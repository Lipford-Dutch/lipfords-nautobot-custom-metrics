# Installing the App in Nautobot

Here you will find detailed instructions on how to **install** and **configure** the App within your Nautobot environment.

## Prerequisites

- The app is compatible with Nautobot 2.0.0 and higher.
- Databases supported: PostgreSQL, MySQL

!!! note
    Please check the [dedicated page](compatibility_matrix.md) for a full compatibility matrix and the deprecation policy.

## Install Guide

!!! note
    Apps can be installed from the [Python Package Index](https://pypi.org/) or locally. See the [Nautobot documentation](https://docs.nautobot.com/projects/core/en/stable/user-guide/administration/installation/app-install/) for more details. The pip package name for this app is [`tns-custom-metrics`](https://pypi.org/project/tns-custom-metrics/).

The app is available as a Python package via PyPI and can be installed with `pip`:

```shell
pip install tns-custom-metrics
```

To ensure Metrics & Monitoring Extension App is automatically re-installed during future upgrades, create a file named `local_requirements.txt` (if not already existing) in the Nautobot root directory (alongside `requirements.txt`) and list the `tns-custom-metrics` package:

```shell
echo tns-custom-metrics >> local_requirements.txt
```

Once installed, the app needs to be enabled in your Nautobot configuration. The following block of code below shows the additional configuration required to be added to your `nautobot_config.py` file:

- Append `"tns_custom_metrics"` to the `PLUGINS` list.
- Append the `"tns_custom_metrics"` dictionary to the `PLUGINS_CONFIG` dictionary and override any defaults.

```python
# In your nautobot_config.py
PLUGINS = ["tns_custom_metrics"]

# PLUGINS_CONFIG = {
#     "tns_custom_metrics": {
#         "app_metrics": {
#             "gitrepositories": True,
#             "jobs": True,
#             "models": {
#                 "dcim": {
#                     "Site": True,
#                     "Rack": True,
#                     "Device": True,
#                     "Interface": True,
#                     "Cable": True,
#                 },
#                 "ipam": {
#                     "IPAddress": True,
#                     "Prefix": True,
#                 },
#                 "extras": {
#                     "GitRepository": True
#                 },
#             },
#             "queues": True,
#             "versions": {
#                 "basic": True,
#                 "plugins": True,
#             }
#         }
#     },
# }
```

Once the Nautobot configuration is updated, run the Post Upgrade command (`nautobot-server post_upgrade`) to run migrations and clear any cache:

```shell
nautobot-server post_upgrade
```

Then restart (if necessary) the Nautobot services which may include:

- Nautobot
- Nautobot Workers
- Nautobot Scheduler

```shell
sudo systemctl restart nautobot nautobot-worker nautobot-scheduler
```

## App Configuration

The app behavior can be controlled with the following list of settings:

| Key     | Example | Default | Description                          |
| ------- | ------ | -------- | ------------------------------------- |
| `app_metrics` | `{"models": {"dcim": "Device": True}}` | `{"models": {"dcim": {"Site": True, "Rack": True, "Device": True}, "ipam": {"IPAddress": True, "Prefix": True}}, "jobs": True, "queues": True, "versions": {"basic": False, "plugins": False}` | Specifies which metrics to publish for each app. |


## Included Grafana Dashboard

Included within this app is a Grafana dashboard which will work with the example configuration above. To install this dashboard import the JSON from [Grafana Dashboard](https://raw.githubusercontent.com/nautobot/tns-custom-metrics/develop/docs/nautobot_grafana_dashboard.json) into Grafana.

![Nautobot Grafana Dashboard](https://raw.githubusercontent.com/nautobot/tns-custom-metrics/develop/docs/images/nautobot_grafana_dashboard.png)
