# TNS Metrics & Monitoring Extension App

Lightweight Nautobot plugin that exposes additional metrics as Prometheus endpoints.

## Documentation

Full project documentation is published on [ReadTheDocs](https://docs.nautobot.com/projects/capacity-metrics/en/latest/) and can be built locally using `invoke mkdocs-serve`.

## Contributing to the Documentation

Contributions are welcome! Refer to [docs/dev/contributing.md](docs/dev/contributing.md) for development guidelines and ensure a changelog fragment is added under `changes/` with every pull request.

## Development Quickstart

Clone the repository, run `./setup.sh`, then execute `pytest -q && coverage html` to run the tests and generate a coverage report.

## Questions

For questions or support please open an issue on GitHub or reach out on the Network to Code Slack.
