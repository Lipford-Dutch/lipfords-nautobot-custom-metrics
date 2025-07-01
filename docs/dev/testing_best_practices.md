# Testing Best Practices

This project encourages writing fast and reliable tests. When adding tests consider the following recommendations:

- **Isolate external dependencies** using `unittest.mock` so tests require no database records or network access.
- **Aim for small focused tests** that validate a single behaviour. This keeps failures easy to diagnose.
- **Use fixtures** to share reusable setup logic. PyTest fixtures reduce duplication and speed up tests.
- **Prefer parametrization** over loops in tests. Parametrized tests clearly show all variations being tested.
- **Measure coverage** regularly and add tests around complex code paths.

These guidelines help maintain a healthy and maintainable test suite.
