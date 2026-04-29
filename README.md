# feedscope

> Async multi-source aggregator (arXiv + Hacker News) — **Project 0 of AI Agent Engineer Path** (Phase 1 capstone).

## Status

Working build — **14 tests passing**, `mypy --strict` clean, `ruff` clean.

## Install

```bash
git clone https://github.com/LovRanRan/feedscope.git
cd feedscope
uv sync
```

Requires Python 3.14+ (auto-managed by `uv`).

## Usage

Fetch articles from multiple sources concurrently:

```bash
uv run feedscope fetch --query "agent" --sources arxiv,hn --limit 20 --output out.json
```

Then:

```bash
cat out.json
# [
#   {
#     "source": "arxiv",
#     "articles": [...],
#     "fetched_at": "2026-04-29T18:30:00+00:00",
#     "error": null
#   },
#   {
#     "source": "hn",
#     "articles": [...],
#     "fetched_at": "2026-04-29T18:30:00+00:00",
#     "error": null
#   }
# ]
```

### CLI options


| Flag              | Default    | Description                          |
| ----------------- | ---------- | ------------------------------------ |
| `--query` / `-q`  | (required) | Search keyword passed to each source |
| `--sources`       | `arxiv,hn` | Comma-separated source names         |
| `--limit` / `-n`  | `20`       | Max results per source               |
| `--output` / `-o` | `out.json` | Output JSON file path                |

### Environment variables

`FetchConfig` is a `pydantic-settings` model — env vars with prefix `FEEDSCOPE_` override CLI defaults:

```bash
FEEDSCOPE_QUERY=ai uv run feedscope fetch    # query=ai if --query not passed
```

## Architecture

```
              CLI (typer)
                  │
                  ▼
            FetchConfig (pydantic-settings)
                  │
                  ▼
            Orchestrator (asyncio.gather + return_exceptions=True)
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
  ArxivFetcher         HNFetcher
   (Atom XML)          (JSON)
        │                   │
        └─────────┬─────────┘
                  ▼
           list[FetchResult]
                  │
                  ▼
         JSON Exporter (model_dump mode=json)
                  │
                  ▼
                out.json
```

### Key components

- **`BaseFetcher`** (`feedscope/fetchers/base.py`) — abstract base class. Constructor injects `httpx.AsyncClient` and `timeout`; subclasses must override `source: ClassVar[SourceName]` and `async def fetch(query, limit) -> FetchResult`. Two concrete subclasses (`ArxivFetcher` / `HNFetcher`) justify the abstraction.
- **Pydantic models** (`feedscope/models.py`, `config.py`):

  - `Article` — frozen, `Annotated[..., Field(min_length=1)]` for `title`, `AwareDatetime` for `published_at`, `HttpUrl` for `url`, `Literal["arxiv", "hn"]` for `source`.
  - `FetchResult` — frozen, contains `list[Article]` plus optional `error: str | None` for failure tracking.
  - `FetchConfig` — `BaseSettings` (env-driven), Pydantic validators reject invalid sources at construction time.
- **`run_fetchers`** (`feedscope/orchestrator.py`) — `asyncio.gather(*[f.fetch(...) for f in fetchers], return_exceptions=True)` runs all fetchers concurrently. Any unexpected exception is converted to `FetchResult(error=...)` so a single source failure does not crash the run. Wall time of N concurrent fetchers ≈ slowest fetcher (verified by `test_orchestrator_runs_fetchers_concurrently`).
- **`write_json`** (`feedscope/exporter.py`) — `model_dump(mode="json")` converts Pydantic objects to JSON-native types (`datetime`/`HttpUrl` → string), then `json.dumps(indent=2)` produces human-readable output.

## Development

```bash
# Run all tests (14 tests across 5 test files)
uv run python -m pytest tests/ -v

# Type check (strict mode + pydantic mypy plugin)
uv run mypy feedscope tests

# Lint + format
uv run ruff check feedscope tests
uv run ruff format feedscope tests
```

### Test layout


| File                          | Tests | What it verifies                                                                     |
| ----------------------------- | ----- | ------------------------------------------------------------------------------------ |
| `tests/test_models.py`        | 3     | Pydantic validators (empty title rejection, unix timestamp parsing, env var loading) |
| `tests/test_arxiv_fetcher.py` | 3     | ArxivFetcher with respx-mocked HTTP (success / empty / 500)                          |
| `tests/test_hn_fetcher.py`    | 3     | HNFetcher with respx-mocked HTTP (success / empty / 500)                             |
| `tests/test_orchestrator.py`  | 3     | `run_fetchers` concurrency, result merging, exception isolation                      |
| `tests/test_cli.py`           | 2     | Typer CLI command registration via`CliRunner`                                        |

## Project 0 acceptance criteria


| Criterion                                      | Status                                                                    |
| ---------------------------------------------- | ------------------------------------------------------------------------- |
| Python 3.11+ via`uv`                           | ✓ (using 3.14)                                                           |
| 1+ class hierarchy with inheritance            | ✓ (`BaseFetcher` → `ArxivFetcher` + `HNFetcher`)                        |
| Type hints everywhere; passes`mypy --strict`   | ✓ (15 source files clean, with`pydantic.mypy` plugin)                    |
| asyncio for ≥1 concurrent operation           | ✓ (`asyncio.gather` in `run_fetchers`)                                   |
| Pydantic models for input config + output rows | ✓ (`FetchConfig` `BaseSettings` + `Article` / `FetchResult` `BaseModel`) |
| CLI built with`typer` or `click`               | ✓ (`typer` with `fetch` sub-command)                                     |
| 5+ pytest tests                                | ✓ (14 tests)                                                             |
| README with example invocation                 | ✓ (this file)                                                            |
| Public GitHub repo, ≥5 commits                | (in progress, Commit 7)                                                   |

## Lessons learned

Five non-obvious takeaways from building this:

1. **Path containing spaces + `src/` layout + editable install is a fragile combination.**
   Working out of `~/Desktop/AI agent Engineer/.../project0/`, the editable install's `.pth` file pointed at `.../src/` correctly, but Python's `site.py` intermittently refused to add the directory to `sys.path` — `import feedscope` would fail despite `uv pip list` confirming the package was installed. I rotated through two build backends (`hatchling` then `uv_build`) before realising the issue was the `src/` indirection itself. Switching to **flat layout** (`feedscope/` directly under the project root, `[tool.uv.build-backend] module-root = ""`) made the entry point stable. Rule of thumb for myself: when a project path contains spaces, default to flat layout, or relocate the project somewhere with no spaces.

2. **Pylance and mypy disagree about Pydantic.**
   Pydantic v2 lets you pass a `str` to an `HttpUrl` field — it converts internally. Pure type checkers refuse this. `pydantic.mypy` plugin teaches **mypy** the conversion, but Pylance (Pyright) has no equivalent plugin and keeps red-lining. I wasted some time chasing red lines that `mypy` had already cleared. Rule of thumb: `mypy` output is acceptance; Pylance is decoration. If `mypy` passes, ignore Pylance's red lines (or selectively suppress with `# pyright: ignore[...]`).

3. **`asyncio.gather(return_exceptions=True)` returns `list[T | BaseException]`, not `list[T]`.**
   Without an `isinstance` narrow, mypy correctly refuses to treat results as `T`. The pattern that ended up clean: `zip` original fetchers with results, `isinstance(result, BaseException)` then synthesize `FetchResult(source=fetcher.source, error=...)`. This is why I added `source: ClassVar[SourceName]` to `BaseFetcher` mid-way — the orchestrator needs the source identifier even when the fetch path raises before producing a `FetchResult`.

4. **`list[X]` is invariant; `Sequence[X]` is covariant.**
   I hit this passing `list[FakeFetcher]` to a function typed `list[BaseFetcher]`. mypy refused — accepting `list[BaseFetcher]` would let the function `append` a non-FakeFetcher into the caller's original list. Switching the signature to `Sequence[BaseFetcher]` (read-only protocol → covariant) fixed it instantly. Internalised heuristic: function parameters that only iterate should be `Sequence` / `Iterable`; only use `list` when the function actually mutates.

5. **Half-DRY is worse than no DRY.**
   When I added `source: ClassVar` and refactored `Article(..., source=self.source)`, I left the four error-branch `FetchResult(source="arxiv", ...)` strings as literals. Result: future renames of the source string would silently desync success vs error paths. The reviewer (Claude) caught it. Lesson: when refactoring for DRY, `grep` for every occurrence of the constant before stopping. Partial wins quietly create future bugs.

## Known limitations

- arXiv API is unauthenticated and rate-limited. Heavy use may return HTTP 429.
- HN Algolia search is full-text — no semantic matching. Phrases like `"agent OR agents"` literal-match.
- No retry / circuit breaker layer (Phase 3 territory).
- No persistence — every run hits the live API. Caching at the fetcher level is left for future iterations.

## License

MIT
