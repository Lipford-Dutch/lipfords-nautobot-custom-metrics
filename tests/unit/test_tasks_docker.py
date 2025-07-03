import types
from unittest.mock import MagicMock

import tasks


def _dummy_context(local=False):
    ctx = types.SimpleNamespace()
    ctx.tns_custom_metrics = types.SimpleNamespace(
        local=local,
        compose_http_timeout="30",
        nautobot_ver="1.0",
        python_ver="3.11",
        project_name="proj",
        compose_dir="/tmp",
        compose_files=["docker-compose.test.yml"],
    )
    ctx.run = MagicMock(return_value=types.SimpleNamespace(stdout=""))
    return ctx


def test_docker_compose_builds_command_and_env():
    ctx = _dummy_context()
    tasks.docker_compose(ctx, "up", service="svc", env={"FOO": "BAR"}, pty=False)
    assert ctx.run.called
    command, kwargs = ctx.run.call_args[0][0], ctx.run.call_args.kwargs
    assert "docker compose" in command
    assert "svc" in command
    assert kwargs["env"]["COMPOSE_HTTP_TIMEOUT"] == "30"
    assert kwargs["env"]["FOO"] == "BAR"


def test_run_command_local_uses_context_run():
    ctx = _dummy_context(local=True)
    tasks.run_command(ctx, "echo hi", pty=False)
    ctx.run.assert_called_with("echo hi", pty=False)


def test_run_command_remote_exec_when_running(monkeypatch):
    ctx = _dummy_context()
    docker_mock = MagicMock()
    docker_mock.side_effect = [
        types.SimpleNamespace(stdout="svc\n"),
        types.SimpleNamespace(stdout="")
    ]
    monkeypatch.setattr(tasks, "docker_compose", docker_mock)
    tasks.run_command(ctx, "cmd", service="svc", pty=False)
    docker_mock.assert_called_with(ctx, "exec svc cmd", pty=False)


def test_run_command_remote_run_when_not_running(monkeypatch):
    ctx = _dummy_context()
    docker_mock = MagicMock()
    docker_mock.side_effect = [
        types.SimpleNamespace(stdout="other\n"),
        types.SimpleNamespace(stdout="")
    ]
    monkeypatch.setattr(tasks, "docker_compose", docker_mock)
    tasks.run_command(ctx, "cmd", service="svc", pty=False)
    docker_mock.assert_called_with(ctx, "run --rm --entrypoint='cmd' svc", pty=False)

