# feedscope

> Async multi-source aggregator (arXiv + Hacker News) — Project 0 of AI Agent Engineer Path.

## Status

In development.

## Install

```bash
uv sync
```

## Usage

> _TBD — fill in after Commit 6 with real CLI examples._

```bash
# Example (placeholder)
feedscope fetch --query "agent" --sources arxiv,hn --limit 20 --output out.json
```

## Architecture

- `BaseFetcher` (abstract) → `ArxivFetcher`, `HNFetcher`
- `Orchestrator` runs fetchers concurrently via `asyncio.gather`
- `Exporter` writes results to JSON

## Development

```bash
# Run tests
uv run pytest

# Lint
uv run ruff check src/ tests/

# Type check
uv run mypy src/
```

## License

MIT.
