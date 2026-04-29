from typing import Any

import httpx
import respx

from feedscope.fetchers.hn import HN_API, HNFetcher

HN_RESPONSE_JSON: dict[str, Any] = {
    "hits": [
        {
            "title": "First Post",
            "url": "https://example.com/1",
            "author": "alice",
            "created_at_i": 1723737138,
            "objectID": "1",
        },
        {
            "title": "Second Post (self-post)",
            "url": None,
            "author": "bob",
            "created_at_i": 1723823538,
            "objectID": "2",
        },
        {
            "title": "Third Post",
            "url": "https://example.com/3",
            "author": "carol",
            "created_at_i": 1723909938,
            "objectID": "3",
        },
    ]
}
HN_EMPTY_JSON: dict[str, Any] = {"hits": []}


@respx.mock
async def test_hn_fetcher_returns_articles_on_success() -> None:
    respx.get(HN_API).mock(return_value=httpx.Response(200, json=HN_RESPONSE_JSON))
    async with httpx.AsyncClient() as client:
        fetcher = HNFetcher(client=client)
        result = await fetcher.fetch("agent", limit=10)
    assert str(result.articles[1].url) == "https://news.ycombinator.com/item?id=2"
    assert result.articles[0].source == "hn"
    assert result.error is None
    assert result.articles[0].authors == ["alice"]
    assert len(result.articles) == 3


@respx.mock
async def test_hn_fetcher_handles_empty_results() -> None:
    respx.get(HN_API).mock(return_value=httpx.Response(200, json=HN_EMPTY_JSON))
    async with httpx.AsyncClient() as client:
        fetcher = HNFetcher(client=client)
        result = await fetcher.fetch("agent", limit=10)
    assert result.source == "hn"
    assert result.articles == []
    assert result.error is None


@respx.mock
async def test_hn_fetcher_returns_error_on_http_500() -> None:
    respx.get(HN_API).mock(return_value=httpx.Response(500))
    async with httpx.AsyncClient() as client:
        fetcher = HNFetcher(client=client)
        result = await fetcher.fetch("agent", limit=10)
    assert result.source == "hn"
    assert result.articles == []
    assert result.error is not None
    assert "HTTP 500" in result.error
