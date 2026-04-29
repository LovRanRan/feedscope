import asyncio
from collections.abc import Sequence

from feedscope.fetchers.arxiv import ArxivFetcher
from feedscope.fetchers.base import BaseFetcher
from feedscope.fetchers.hn import HNFetcher
from feedscope.models import FetchResult, SourceName

FETCHERS: dict[SourceName, type[BaseFetcher]] = {
    "arxiv": ArxivFetcher,
    "hn": HNFetcher,
}


async def run_fetchers(
    fetchers: Sequence[BaseFetcher],
    query: str,
    limit: int,
) -> list[FetchResult]:
    results = await asyncio.gather(
        *[f.fetch(query, limit) for f in fetchers],
        return_exceptions=True,
    )
    # 2. 异常兜底转 FetchResult
    final: list[FetchResult] = []
    for fetcher, result in zip(fetchers, results, strict=True):
        if isinstance(result, BaseException):
            final.append(FetchResult(source=fetcher.source, error=f"Unexpected: {result}"))
        else:
            final.append(result)
    return final
