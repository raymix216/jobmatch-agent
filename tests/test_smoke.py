"""Smoke tests for the M0 skeleton."""


def test_import():
    import jobmatch

    assert jobmatch.__version__ == "0.1.0"


def test_health_command(capsys):
    from jobmatch.__main__ import main

    assert main(["health"]) == 0
    out = capsys.readouterr().out
    assert "jobmatch-agent" in out


def test_settings_defaults():
    from jobmatch.config import settings

    assert settings.app_name == "jobmatch-agent"
