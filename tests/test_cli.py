from typer.testing import CliRunner

from feedscope.cli import app


def test_cli_help_lists_fetch_command() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "fetch" in result.stdout
    assert "hello" in result.stdout

def test_cli_fetch_help_shows_query_option() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["fetch", "--help"])
    assert result.exit_code == 0
    assert "--query" in result.stdout
    assert "--sources" in result.stdout
    assert "Search keyword" in result.stdout
