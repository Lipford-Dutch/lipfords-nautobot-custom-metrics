"""Tests for Docker-related invoke tasks."""

import tempfile
import types
from unittest.mock import MagicMock

import pytest

pytestmark = pytest.mark.unit

pytest.importorskip("invoke")  # noqa: E402

import tasks  # noqa: E402


@pytest.fixture()
def dummy_ctx():
    """Return a stub context for invoking docker-compose commands."""

    def _make(local=False):
        ctx = types.SimpleNamespace()
        ctx.tns_custom_metrics = types.SimpleNamespace(
            local=local,
            compose_http_timeout="30",
            nautobot_ver="1.0",
            python_ver="3.11",
            project_name="proj",
            compose_dir=tempfile.gettempdir(),
            compose_files=["docker-compose.test.yml"],
        )
        ctx.run = MagicMock(return_value=types.SimpleNamespace(stdout=""))
        return ctx

    return _make


def test_docker_compose_builds_command_and_env(dummy_ctx):
    """Verify docker compose command construction and env passthrough."""
    ctx = dummy_ctx()
    tasks.docker_compose(ctx, "up", service="svc", env={"FOO": "BAR"}, pty=False)
    assert ctx.run.called  # noqa: S101
    command, kwargs = ctx.run.call_args[0][0], ctx.run.call_args.kwargs
    assert "docker compose" in command  # noqa: S101
    assert "svc" in command  # noqa: S101
    assert kwargs["env"]["COMPOSE_HTTP_TIMEOUT"] == "30"  # noqa: S101
    assert kwargs["env"]["FOO"] == "BAR"  # noqa: S101


def test_run_command_local_uses_context_run(dummy_ctx):
    """Ensure ``run_command`` executes locally when configured."""
    ctx = dummy_ctx(local=True)
    tasks.run_command(ctx, "echo hi", pty=False)
    ctx.run.assert_called_with("echo hi", pty=False)


def test_run_command_remote_exec_when_running(dummy_ctx, monkeypatch):
    """Remote command uses ``exec`` when container running."""
    ctx = dummy_ctx()
    docker_mock = MagicMock()
    docker_mock.side_effect = [
        types.SimpleNamespace(stdout="svc\n"),
        types.SimpleNamespace(stdout=""),
    ]
    monkeypatch.setattr(tasks, "docker_compose", docker_mock)
    tasks.run_command(ctx, "cmd", service="svc", pty=False)
    docker_mock.assert_called_with(ctx, "exec svc cmd", pty=False)


def test_run_command_remote_run_when_not_running(dummy_ctx, monkeypatch):
    """Remote command uses ``run`` when container is absent."""
    ctx = dummy_ctx()
    docker_mock = MagicMock()
    docker_mock.side_effect = [
        types.SimpleNamespace(stdout="other\n"),
        types.SimpleNamespace(stdout=""),
    ]
    monkeypatch.setattr(tasks, "docker_compose", docker_mock)
    tasks.run_command(ctx, "cmd", service="svc", pty=False)
    docker_mock.assert_called_with(ctx, "run --rm --entrypoint='cmd' svc", pty=False)
