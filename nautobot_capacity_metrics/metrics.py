"""Metrics libraries for the nautobot_capacity_metrics app."""

import importlib
import logging
import platform
from collections.abc import Iterable
from copy import deepcopy

import django
from django.conf import settings
from nautobot.extras.choices import JobResultStatusChoices
from packaging import version
from django.utils import timezone
from django.db.models import Count, Avg, F
from prometheus_client.core import GaugeMetricFamily, Metric, CounterMetricFamily
from django.db import models
from django.contrib.auth.models import AbstractUser
from nautobot.extras.models import JobResult UserInteraction APIRequest SessionRecord FeatureUsage   # pylint: disable=import-outside-toplevel,no-name-in-module
logger = logging.getLogger(__name__)

nautobot_version = version.parse(settings.VERSION)

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG["nautobot_capacity_metrics"]["app_metrics"]


def metric_jobs(type_of_job):
    """Return Jobs results in Prometheus Metric format.

    Return:
        Iterator[GaugeMetricFamily]
            nautobot_job_task_stats: with jobs module, name, task name and status as labels
        Iterator[GaugeMetricFamily]
            nautobot_job_execution_status: with jobs module the name and overall status of the job
    """
    

    git_repo_job_prefix = "nautobot.core.jobs.GitRepository"

    # Get the latest result for each job
    if type_of_job == "job":
        job_results = (
            JobResult.objects.exclude(task_name__startswith=git_repo_job_prefix)
            .order_by("name", "-date_done")
            .distinct("name")
        )
    elif type_of_job == "git_repository":
        job_results = (
            JobResult.objects.filter(task_name__startswith=git_repo_job_prefix)
            .order_by("name", "-date_done")
            .distinct("name")
        )
    else:
        raise ValueError(f"Unknown type of job {type_of_job} - choose from 'job' or 'git_repository.")

    # Each Job can have multiple jobs (tasks) with individual statistics success, warning, failure,
    # info the stats gauge exposes these
    task_stats_gauge = GaugeMetricFamily(
        f"nautobot_{type_of_job}_task_stats",
        f"Per {type_of_job.title()} task statistics",
        labels=["module", "name", "status"],
    )

    # Each job has an overall status, one status per high level job not per task, which is one of pending,
    # running, completed, errored or failed as defined in the JobResultStatusChoices class
    execution_status_gauge = GaugeMetricFamily(
        f"nautobot_{type_of_job}_execution_status",
        f"{type_of_job.title()} completion status",
        labels=["module", "status"],
    )

    for job in job_results:
        # Add metrics for the overall job status
        for status_name, _ in JobResultStatusChoices:
            if job.status == status_name:
                execution_status_gauge.add_metric([job.name, status_name], 1)
            else:
                execution_status_gauge.add_metric([job.name, status_name], 0)

    yield task_stats_gauge
    yield execution_status_gauge


def metric_models(params):
    """Return Models count in Prometheus Metric format.

    Args:
        params (dict): list of models to return organized per application

    Return:
        Iterator[GaugeMetricFamily]
            nautobot_model_count: with model name and application name as labels
    """
    gauge = GaugeMetricFamily("nautobot_model_count", "Per Nautobot Model count", labels=["app", "name"])
    for app in params:
        app_config = deepcopy(params[app])  # Avoid changing the dictionary we are iterating over
        module = app_config.pop("_module", "nautobot")
        for model in app_config:
            try:
                models = importlib.import_module(f"{module}.{app}.models")
                model_class = getattr(models, model)
                gauge.add_metric([app, model], model_class.objects.count())
            except ModuleNotFoundError:
                logger.warning("Unable to find the python library %s.models", app)
            except AttributeError:
                logger.warning("Unable to load the module %s from the python library %s.models", model, app)

    yield gauge


def metric_versions():
    """Return django, Nautobot, Python and app versions in Prometheus Metric format.

    Return:
        Iterator[GaugeMetricFamily]
            nautobot_app_versions: the versions as labels
    """
    versions = {}
    if PLUGIN_SETTINGS["versions"]["basic"]:
        versions.update(
            {"python": platform.python_version(), "django": django.get_version(), "nautobot": settings.VERSION}
        )

    # Collect app versions
    if PLUGIN_SETTINGS["versions"]["plugins"]:
        for app in settings.PLUGINS:
            try:
                app_module = importlib.import_module(app)
            except ModuleNotFoundError:
                logger.warning("Unable to find the python library %s", app)
                continue
            try:
                versions[app] = app_module.__version__
            except AttributeError:
                logger.warning("Module %s does not have __version__ defined.", app)
    gauge = GaugeMetricFamily("nautobot_app_versions", "Nautobot app versions", labels=versions.keys())
    gauge.add_metric(versions.values(), 1)
    yield gauge


# Reference: NAC-1725, Sprint 37

# 1. Active Users

def collect_daily_active_users():
    """
    Gauge: nautobot_user_dau{date,team,device_vendor,device_type}
    Unique users interacting (UI + API) in last 7-day window by team and device.
    """
    today = timezone.now().date()
    week_ago = today - timezone.timedelta(days=7)
    qs = (
        UserInteraction.objects.filter(
            timestamp__date__gte=week_ago,
            event_type__in=['ui','api']
        )
        .values('timestamp__date', 'user__team', 'device_vendor', 'device_type')
        .annotate(count=Count('user', distinct=True))
    )
    gauge = GaugeMetricFamily(
        'nautobot_user_dau',
        'Unique daily active users over 7-day window',
        labels=['date','team','device_vendor','device_type'],
    )
    for e in qs:
        gauge.add_metric([
            e['timestamp__date'].isoformat(),
            e['user__team'],
            e.get('device_vendor') or 'unknown',
            e.get('device_type') or 'unknown'
        ], e['count'])
    yield gauge


def collect_monthly_active_users():
    """
    Gauge: nautobot_user_mau{month,team,device_vendor,device_type}
    Unique monthly active users (UI + API) with MoM comparisons.
    """
    now = timezone.now()
    month_start = now.replace(day=1).date()
    qs = (
        UserInteraction.objects.filter(
            timestamp__date__gte=month_start,
            event_type__in=['ui','api']
        )
        .values('user__team', 'device_vendor', 'device_type')
        .annotate(count=Count('user', distinct=True))
    )
    gauge = GaugeMetricFamily(
        'nautobot_user_mau',
        'Unique monthly active users',
        labels=['month','team','device_vendor','device_type'],
    )
    for e in qs:
        gauge.add_metric([
            f"{now.year}-{now.month:02d}",
            e['user__team'],
            e.get('device_vendor') or 'unknown',
            e.get('device_type') or 'unknown'
        ], e['count'])
    yield gauge


def collect_dau_mau_ratio():
    """
    Gauge: nautobot_user_dau_mau_ratio{date,team}
    Daily DAU/MAU ratio, segmented by team, updated daily.
    """
    today = timezone.now().date().isoformat()
    teams = User.objects.values_list('team', flat=True).distinct()
    gauge = GaugeMetricFamily(
        'nautobot_user_dau_mau_ratio',
        'Daily DAU/MAU ratio',
        labels=['date','team'],
    )
    for team in teams:
        dau = UserInteraction.objects.filter(
            timestamp__date=timezone.now().date(),
            event_type__in=['ui','api'],
            user__team=team
        ).values('user').distinct().count()
        now = timezone.now()
        mau = UserInteraction.objects.filter(
            timestamp__year=now.year,
            timestamp__month=now.month,
            event_type__in=['ui','api'],
            user__team=team
        ).values('user').distinct().count()
        ratio = dau/mau if mau else 0
        gauge.add_metric([today,team],ratio)
    yield gauge

# 2. Session Metrics

def collect_session_duration():
    """
    Gauge: nautobot_session_avg_duration_seconds{interval,team}
    Average session duration in seconds over 7-day and 30-day windows, segmented by team.
    """
    now = timezone.now()
    windows = {
        '7d': now - timezone.timedelta(days=7),
        '30d': now - timezone.timedelta(days=30),
    }
    gauge = GaugeMetricFamily(
        'nautobot_session_avg_duration_seconds',
        'Average session duration in seconds',
        labels=['interval','team'],
    )
    for label, since in windows.items():
        qs = (
            SessionRecord.objects.filter(start__gte=since)
            .annotate(duration=F('end') - F('start'))
            .values('user__team')
            .annotate(avg=Avg('duration'))
        )
        for e in qs:
            secs = e['avg'].total_seconds() if e['avg'] else 0
            gauge.add_metric([label, e['user__team']], secs)
    yield gauge


def collect_session_frequency():
    """
    Gauge: nautobot_sessions_per_user{user,team}
    Number of sessions per user (all time). Admins filter via Prometheus query range.
    """
    qs = (
        SessionRecord.objects.values('user_id','user__team')
        .annotate(count=Count('id'))
    )
    gauge = GaugeMetricFamily(
        'nautobot_sessions_per_user',
        'Total sessions per user by team',
        labels=['user','team'],
    )
    for e in qs:
        gauge.add_metric([str(e['user_id']), e['user__team']], e['count'])
    yield gauge

# 3. Feature Usage

def collect_top_features_used():
    """
    Gauge: nautobot_feature_usage_top{feature,interval,team,user,module}
    Top 10 features by usage count in 7-day and 30-day windows, segmented.
    """
    now = timezone.now()
    windows = {'7d': now - timezone.timedelta(days=7), '30d': now - timezone.timedelta(days=30)}
    gauge = GaugeMetricFamily(
        'nautobot_feature_usage_top',
        'Top features by usage count',
        labels=['feature','interval','team','user','module'],
    )
    for label, since in windows.items():
        qs = (
            FeatureUsage.objects.filter(timestamp__gte=since)
            .values('feature_name','user__team','user_id','module')
            .annotate(count=Count('id'))
            .order_by('-count')[:10]
        )
        for e in qs:
            gauge.add_metric([
                e['feature_name'], label, e['user__team'], str(e['user_id']), e['module']
            ], e['count'])
    yield gauge


def collect_feature_adoption_rate():
    """
    Gauge: nautobot_feature_adoption_rate{feature,team}
    % of users adopting each new feature within 30 days, segmented by team.
    """
    total = User.objects.count()
    gauge = GaugeMetricFamily(
        'nautobot_feature_adoption_rate',
        'Feature adoption rate within 30 days',
        labels=['feature','team'],
    )
    for feature in FeatureRelease.objects.all():
        window_end = feature.release_date + timezone.timedelta(days=30)
        qs = (
            FeatureUsage.objects.filter(
                feature_name=feature.name,
                timestamp__range=(feature.release_date, window_end)
            )
            .values('user__team')
            .annotate(adopters=Count('user', distinct=True))
        )
        for e in qs:
            rate = e['adopters']/total if total else 0
            gauge.add_metric([feature.name, e['user__team']], rate)
    yield gauge

# 4. User Actions

def collect_user_logins():
    """
    Gauge: nautobot_user_logins_total{user,team}
    Total login count per user, segmented by team; windows via PromQL.
    """
    qs = (
        UserInteraction.objects.filter(event_type='login')
        .values('user_id','user__team')
        .annotate(total=Count('id'))
    )
    gauge = GaugeMetricFamily(
        'nautobot_user_logins_total',
        'Total user login count',
        labels=['user','team'],
    )
    for e in qs:
        gauge.add_metric([str(e['user_id']), e['user__team']], e['total'])
    yield gauge


def collect_api_calls():
    """
    Gauge: nautobot_api_requests_total{endpoint,interval,team}
    API call counts per endpoint in 7-day and 30-day windows, segmented by team.
    """
    now = timezone.now()
    windows = {'7d': now - timezone.timedelta(days=7), '30d': now - timezone.timedelta(days=30)}
    gauge = GaugeMetricFamily(
        'nautobot_api_requests_total',
        'API calls per endpoint',
        labels=['endpoint','interval','team'],
    )
    for label, since in windows.items():
        qs = (
            APIRequest.objects.filter(timestamp__gte=since)
            .values('endpoint','user__team')
            .annotate(total=Count('id'))
        )
        for e in qs:
            gauge.add_metric([e['endpoint'], label, e['user__team']], e['total'])
    yield gauge
