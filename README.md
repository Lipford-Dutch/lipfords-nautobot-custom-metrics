# TNS Metrics & Monitoring App

A Nautobot plugin that exposes additional Prometheus metrics and allows custom metrics for your deployment.

## Features

- Adds `/api/plugins/capacity-metrics/app-metrics` endpoint with Git repository, job, queue and model statistics.
- Register your own metrics via `register_metric_func` or `PLUGINS_CONFIG`.
- Docker-based development environment managed by Poetry and Invoke.

## Quick Install

```shell
pip install tns-custom-metrics
```

Update `nautobot_config.py`:

```python
PLUGINS = ["tns_custom_metrics"]
PLUGINS_CONFIG = {"tns_custom_metrics": {"app_metrics": {}}}
```

Run migrations and restart Nautobot:

```shell
nautobot-server post_upgrade
sudo systemctl restart nautobot nautobot-worker nautobot-scheduler
```

## Development Environment

```shell
poetry shell
poetry install
cp development/creds.example.env development/creds.env
invoke build && invoke start
```

Visit <http://localhost:8080> for Nautobot and <http://localhost:8001> for docs.

## Custom Metrics

See [`docs/user/app_use_cases.md`](docs/user/app_use_cases.md) for examples of registering custom metrics.

## Documentation

Additional documentation is located in the `docs/` directory or online at [docs.nautobot.com](https://docs.nautobot.com/projects/capacity-metrics/).

## Contributing

Run Ruff and tests before committing:

```shell
ruff tns_custom_metrics tests
pytest -q
```

Coverage reports can be generated with `coverage html`.

## License

Licensed under the [Apache 2.0 License](LICENSE).
