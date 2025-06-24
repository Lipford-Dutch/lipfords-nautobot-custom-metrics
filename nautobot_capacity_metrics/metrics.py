"""Metrics libraries for the nautobot_capacity_metrics app."""

import importlib
import logging
import platform
from collections.abc import Iterable
from copy import deepcopy

import django
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Avg, Count, F
from django.utils import timezone
from nautobot.extras.choices import JobResultStatusChoices
from packaging import version
from prometheus_client import Counter, Gauge, Histogram
from prometheus_client.core import GaugeMetricFamily, Metric

logger = logging.getLogger(__name__)

nautobot_version = version.parse(settings.VERSION)

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG["nautobot_capacity_metrics"]["app_metrics"]

User = get_user_model()

try:  # Optional models for user engagement metrics
    from .models import (
        APIRequest,
        FeatureRelease,
        FeatureUsage,
        SessionRecord,
        UserInteraction,
        UserLogin,
    )
except Exception:  # pragma: no cover - models may not be present
    APIRequest = FeatureRelease = FeatureUsage = SessionRecord = UserInteraction = UserLogin = None


def metric_jobs(type_of_job):
    """Return Jobs results in Prometheus Metric format.

    Return:
        Iterator[GaugeMetricFamily]
            nautobot_job_task_stats: with jobs module, name, task name and status as labels
        Iterator[GaugeMetricFamily]
            nautobot_job_execution_status: with jobs module the name and overall status of the job
    """
    from nautobot.extras.models import JobResult  # pylint: disable=import-outside-toplevel,no-name-in-module

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


def collect_extras_metric(funcs):
    """Collect Third party functions to generate additional Metrics.

    Args:
        funcs (list): list of functions to execute

    Return:
        List[GaugeMetricFamily]
            nautobot_model_count: with model name and application name as labels
    """
    for func in funcs:
        if not callable(func):
            logger.warning("Extra metric is not a function, skipping ... ")
            continue

        results = func()

        if not isinstance(results, Iterable):
            logger.warning("Extra metric didn't return a list, skipping ... ")
            continue

        for metric in results:
            if Metric not in type(metric).__bases__:
                logger.warning("Extra metric didn't return a Metric object, skipping ... ")
                continue
            yield metric



#------------------------------------------------------------------------------
# 2. DevOps Automation & Deployment Metrics
#------------------------------------------------------------------------------


# Deployment frequency (e.g., number of deployments per day/week)
ntc_deployment_frequency = Gauge(
    'ntc_devops_deployment_frequency',
    'Number of deployments (e.g., per day) to production.'
)


# Change failure rate (percentage of changes/deployments that fail or require rollback)
ntc_change_failure_rate = Gauge(
    'ntc_devops_change_failure_rate',
    'Percentage of changes or deployments that fail.'
)


# Mean time to recover (MTTR) for incidents
ntc_mttr = Gauge(
    'ntc_devops_mttr',
    'Mean time to recover from incidents in minutes.'
)


# Automation efficiency (percentage of tasks automated vs. manual)
ntc_automation_efficiency = Gauge(
    'ntc_devops_automation_efficiency',
    'Percentage of processes or tasks automated vs. manual.'
)


#------------------------------------------------------------------------------
# 3. User Engagement & Application Metrics
#------------------------------------------------------------------------------


# Active user sessions in the application (could be labeled by environment, role, etc.)
ntc_user_session_count = Gauge(
    'ntc_user_session_count',
    'Number of concurrent or active user sessions.',
    labelnames=['environment', 'role']
)


# Page load or workflow duration times (aggregated or average)
ntc_user_page_load_time = Gauge(
    'ntc_user_page_load_time',
    'Average page load or workflow duration time (ms).'
)


# Tracks user interactions or clicks for telemetry
ntc_user_click_events = Counter(
    'ntc_user_click_events',
    'Count of key user interactions or click events (increment only).'
)


#------------------------------------------------------------------------------
# 4. Plugin & Integration Metrics
#------------------------------------------------------------------------------


# Job volume for a given plugin (e.g., Golden Config, SSoT, etc.)
ntc_plugin_job_volume = Counter(
    'ntc_plugin_job_volume',
    'Count of jobs run by a given plugin.',
    labelnames=['plugin_name']
)


# Success rate or fraction for plugin jobs
ntc_plugin_job_success_rate = Gauge(
    'ntc_plugin_job_success_rate',
    'Success rate (0-1) for plugin jobs.',
    labelnames=['plugin_name']
)


# Execution time (seconds) for plugin jobs
ntc_plugin_job_execution_time = Histogram(
    'ntc_plugin_job_execution_time',
    'Histogram of execution times (in seconds) for plugin jobs.',
    labelnames=['plugin_name'],
    buckets=[0.5, 1.0, 2.0, 5.0, 10.0, 30.0, 60.0, 120.0, float('inf')]
)


# Integration-specific metrics:
#  A. Golden Config Status
ntc_integration_golden_config_status = Gauge(
    'ntc_integration_golden_config_status',
    'Tracks the latest Golden Config job status (0=failure,1=success).',
    labelnames=['device_name']
)


#  B. SSoT Sync Time
ntc_integration_ssot_sync_time = Histogram(
    'ntc_integration_ssot_sync_time',
    'Time taken (in seconds) for SSoT syncs to complete.',
    buckets=[1.0, 5.0, 10.0, 30.0, 60.0, 120.0, float('inf')]
)


#  C. FSD-LVC Job Outcome
ntc_integration_fsd_lvc_job_outcome = Gauge(
    'ntc_integration_fsd_lvc_job_outcome',
    'Tracks the outcome of FSD-LVC job runs (0=failure,1=success).'
)


# Future integrations (APIs, WebHooks, etc.)
ntc_integration_api_call_volume = Counter(
    'ntc_integration_api_call_volume',
    'Number of calls made to external or internal APIs.'
)


ntc_integration_webhook_event_rate = Counter(
    'ntc_integration_webhook_event_rate',
    'Number of webhook events processed.'
)


#------------------------------------------------------------------------------
# 5. Compliance & Configuration Metrics
#------------------------------------------------------------------------------


# Compliance ratio (percentage or fraction)
ntc_compliance_ratio = Gauge(
    'ntc_compliance_ratio',
    'Overall compliance ratio across device/config checks.'
)


# Failed compliance checks
ntc_failed_compliance_checks = Gauge(
    'ntc_failed_compliance_checks',
    'Number of failed compliance checks.'
)


# ---------------------------------------------------------------------------
# User4 Engagement Key Metrics
# ---------------------------------------------------------------------------


def collect_daily_active_users():
    """Collect the Daily Active Users metric."""
    today = timezone.now().date()
    dau = (
        UserInteraction.objects.filter(timestamp__date=today)
        .values('user_id')
        .distinct()
        .count()
    )
    gauge = GaugeMetricFamily(
        'nautobot_user_dau',
        'Number of unique daily active users',
        labels=['date'],
    )
    gauge.add_metric([today.isoformat()], dau)
    yield gauge


def collect_monthly_active_users():
    """Collect the Monthly Active Users metric."""
    now = timezone.now()
    mau = (
        UserInteraction.objects.filter(
            timestamp__year=now.year,
            timestamp__month=now.month,
        )
        .values('user_id')
        .distinct()
        .count()
    )
    gauge = GaugeMetricFamily(
        'nautobot_user_mau',
        'Number of unique monthly active users',
        labels=['month'],
    )
    gauge.add_metric([f"{now.year}-{now.month:02d}"], mau)
    yield gauge


def collect_dau_mau_ratio():
    """Calculate the DAU/MAU ratio."""
    today = timezone.now().date()
    dau = (
        UserInteraction.objects.filter(timestamp__date=today)
        .values('user_id')
        .distinct()
        .count()
    )
    now = timezone.now()
    mau = (
        UserInteraction.objects.filter(
            timestamp__year=now.year,
            timestamp__month=now.month,
        )
        .values('user_id')
        .distinct()
        .count()
    )
    ratio = dau / mau if mau else 0
    gauge = GaugeMetricFamily(
        'nautobot_user_dau_mau_ratio',
        'Daily DAU/MAU ratio',
        labels=['date'],
    )
    gauge.add_metric([today.isoformat()], ratio)
    yield gauge


def collect_session_duration():
    """Track average session duration weekly and monthly."""
    now = timezone.now()
    week_ago = now - timezone.timedelta(days=7)
    avg_week = (
        SessionRecord.objects.filter(start__gte=week_ago)
        .annotate(duration=F('end') - F('start'))
        .aggregate(avg=Avg('duration'))['avg']
    )
    avg_week = avg_week.total_seconds() if avg_week else 0
    month_start = now.replace(day=1)
    avg_month = (
        SessionRecord.objects.filter(start__gte=month_start)
        .annotate(duration=F('end') - F('start'))
        .aggregate(avg=Avg('duration'))['avg']
    )
    avg_month = avg_month.total_seconds() if avg_month else 0
    gauge = GaugeMetricFamily(
        'nautobot_session_avg_duration_seconds',
        'Average session duration in seconds',
        labels=['period'],
    )
    gauge.add_metric(['weekly'], avg_week)
    gauge.add_metric(['monthly'], avg_month)
    yield gauge


def collect_session_frequency():
    """Count sessions per user, segmented by role."""
    qs = SessionRecord.objects.values('user__role').annotate(count=Count('id'))
    gauge = GaugeMetricFamily(
        'nautobot_sessions_per_user',
        'Number of sessions per user by role',
        labels=['user_role'],
    )
    for entry in qs:
        gauge.add_metric([entry['user__role']], entry['count'])
    yield gauge


def collect_top_features_used():
    """Return a ranked list of most-used features."""
    qs = (
        FeatureUsage.objects.values('feature_name')
        .annotate(count=Count('id'))
        .order_by('-count')[:10]
    )
    gauge = GaugeMetricFamily(
        'nautobot_feature_usage_top',
        'Top features used sorted by usage count',
        labels=['feature'],
    )
    for entry in qs:
        gauge.add_metric([entry['feature_name']], entry['count'])
    yield gauge


def collect_feature_adoption_rate():
    """Calculate the adoption rate for new features."""
    for feature in FeatureRelease.objects.all():
        window_end = feature.release_date + timezone.timedelta(days=30)
        adopters = (
            FeatureUsage.objects.filter(
                feature_name=feature.name,
                timestamp__range=(feature.release_date, window_end),
            )
            .values('user_id')
            .distinct()
            .count()
        )
        total = User.objects.count()
        rate = adopters / total if total else 0
        gauge = GaugeMetricFamily(
            'nautobot_feature_adoption_rate',
            'Adoption rate of feature within 30 days',
            labels=['feature'],
        )
        gauge.add_metric([feature.name], rate)
        yield gauge


def collect_user_logins():
    """Log each user login with a timestamp."""
    qs = UserLogin.objects.values('user_id').annotate(total=Count('id'))
    gauge = GaugeMetricFamily(
        'nautobot_user_logins_total',
        'Total number of logins per user',
        labels=['user_id'],
    )
    for entry in qs:
        gauge.add_metric([str(entry['user_id'])], entry['total'])
    yield gauge


def collect_api_calls():
    """Count API calls per endpoint."""
    qs = APIRequest.objects.values('endpoint').annotate(total=Count('id'))
    gauge = GaugeMetricFamily(
        'nautobot_api_requests_total',
        'Total API calls per endpoint',
        labels=['endpoint'],
    )
    for entry in qs:
        gauge.add_metric([entry['endpoint']], entry['total'])
    yield gauge
