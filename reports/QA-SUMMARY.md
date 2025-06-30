# QA Summary

## Local Setup

Run tests and checks using `tox -e qa`.
Example GitHub Actions workflow:
```yaml
jobs:
  qa:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install tox
      - run: tox -e qa
```
```

## Results

| Metric | Value |
| ------ | ----- |
| Coverage | 43% |
| Mutation | n/a (mutmut failed) |
| Ruff | pass |
| Mypy | fail |
