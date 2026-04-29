import httpx
import respx

from feedscope.fetchers.arxiv import ARXIV_API, ArxivFetcher

ARXIV_RESPONSE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2408.12345</id>
    <title>Test Paper One</title>
    <summary>Abstract one.</summary>
    <published>2024-08-15T17:32:18Z</published>
    <author><name>Alice</name></author>
    <author><name>Bob</name></author>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2408.67890</id>
    <title>Test Paper Two</title>
    <summary>Abstract two.</summary>
    <published>2024-08-16T10:00:00Z</published>
    <author><name>Carol</name></author>
  </entry>
</feed>"""
ARXIV_EMPTY_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
</feed>"""

@respx.mock
async def test_arxiv_fetcher_returns_articles_on_success() -> None:
    respx.get(ARXIV_API).mock(return_value=httpx.Response(200, text=ARXIV_RESPONSE_XML))
    async with httpx.AsyncClient() as client:
        fetcher = ArxivFetcher(client=client)
        result = await fetcher.fetch("agent", limit=10)
    assert result.source == "arxiv"
    assert result.error is None
    assert len(result.articles) == 2
    assert result.articles[0].title == "Test Paper One"
    assert result.articles[0].authors == ["Alice", "Bob"]
    assert result.articles[1].title == "Test Paper Two"

@respx.mock
async def test_arxiv_fetcher_handles_empty_results() -> None:
    respx.get(ARXIV_API).mock(return_value=httpx.Response(200, text=ARXIV_EMPTY_XML))
    async with httpx.AsyncClient() as client:
        fetcher = ArxivFetcher(client=client)
        result = await fetcher.fetch("agent", limit=10)
    assert result.source == "arxiv"
    assert result.articles == []
    assert result.error is None


@respx.mock
async def test_arxiv_fetcher_returns_error_on_http_500() -> None:
    respx.get(ARXIV_API).mock(return_value=httpx.Response(500))
    async with httpx.AsyncClient() as client:
        fetcher = ArxivFetcher(client=client)
        result = await fetcher.fetch("agent", limit=10)
    assert result.source == "arxiv"
    assert result.articles == []
    assert result.error is not None
    assert "HTTP 500" in result.error




