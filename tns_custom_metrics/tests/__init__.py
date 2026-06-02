"""Unit and integration tests for the tns_custom_metrics app.

These tests are designed to run inside a configured Nautobot environment, i.e.
via ``nautobot-server test tns_custom_metrics`` (or ``invoke unittest``), which
loads settings from ``NAUTOBOT_CONFIG`` and provisions an isolated test
database. Settings are intentionally *not* configured here so the active
Nautobot configuration is always used.
"""
