import asyncio
import time

from feedscope.fetchers.base import BaseFetcher
from feedscope.models import Article, FetchResult
from feedscope.orchestrator import run_fetchers

SAMPLE_ARTICLE = Article.model_validate(
    {
        "title": "Test Article",
        "url": "https://example.com",
        "source": "arxiv",
        "published_at": "2024-08-15T15:52:18Z",
    }
)


class FakeFetcher(BaseFetcher):
    source = "arxiv"  # 固定, test 不验 source 字段

    def __init__(
        self,
        articles: list[Article],
        delay: float = 0.0,
        should_raise: bool = False,
    ) -> None:
        self._articles = articles
        self._delay = delay
        self._should_raise = should_raise

    async def fetch(self, query: str, limit: int) -> FetchResult:
        if self._delay > 0:
            await asyncio.sleep(self._delay)
        if self._should_raise:
            raise RuntimeError("simulated fetcher bug")
        return FetchResult(source=self.source, articles=self._articles)


async def test_orchestrator_runs_fetchers_concurrently() -> None:
    fetchers = [
        FakeFetcher(articles=[], delay=0.1),
        FakeFetcher(articles=[], delay=0.1),
    ]
    start = time.perf_counter()
    results = await run_fetchers(fetchers, query="test", limit=10)
    elapsed = time.perf_counter() - start
    assert elapsed < 0.15
    assert len(results) == 2


async def test_orchestrator_isolates_exceptions() -> None:
    fetchers = [
        FakeFetcher(articles=[SAMPLE_ARTICLE]),
        FakeFetcher(articles=[], should_raise=True),
    ]
    results = await run_fetchers(fetchers, query="test", limit=10)
    assert len(results) == 2
    # 第一个正常
    assert len(results[0].articles) == 1
    assert results[0].error is None
    # 第二个出错被兜底
    assert results[1].articles == []
    assert results[1].error is not None
    assert "simulated fetcher bug" in results[1].error


async def test_orchestrator_returns_all_results() -> None:
    fetchers = [
        FakeFetcher(articles=[SAMPLE_ARTICLE, SAMPLE_ARTICLE]),
        FakeFetcher(articles=[SAMPLE_ARTICLE, SAMPLE_ARTICLE]),
    ]
    results = await run_fetchers(fetchers, query="test", limit=10)
    assert len(results) == 2
    total = sum(len(r.articles) for r in results)
    assert total == 4
    for r in results:
        assert r.error is None
