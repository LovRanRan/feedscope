import asyncio
from pathlib import Path

import httpx
import typer

from feedscope.config import FetchConfig
from feedscope.exporter import write_json
from feedscope.models import FetchResult
from feedscope.orchestrator import FETCHERS, run_fetchers

app = typer.Typer(help="feedscope: async multi-source aggregator")


@app.command()
def hello() -> None:
    """Placeholder command — kept to enable typer's sub-command mode."""
    typer.echo("feedscope alive.")

@app.command()
def fetch(
    query: str = typer.Option(..., "--query", "-q", help="Search keyword"),
    sources: str = typer.Option("arxiv,hn", "--sources", help="Comma-separated source names"),
    limit: int = typer.Option(20, "--limit", "-n", help="Max results per source"),
    output: Path = typer.Option("out.json", "--output", "-o", help="Output JSON file"),
) -> None:
    """Fetch articles from multiple sources concurrently and write JSON."""
    config = FetchConfig.model_validate({
        "query": query,
        "sources": [s.strip() for s in sources.split(",")],
        "limit": limit,
        "output_path": output,
    })
    results = asyncio.run(_run_fetch(config))
    write_json(results, output)
    typer.echo(f"Wrote {len(results)} results to {output}")

async def _run_fetch(config: FetchConfig) -> list[FetchResult]:
    async with httpx.AsyncClient() as client:
        fetchers = [FETCHERS[s](client=client) for s in config.sources]
        return await run_fetchers(fetchers, config.query, config.limit)

if __name__ == "__main__":
    app()
