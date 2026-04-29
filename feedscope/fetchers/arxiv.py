import xml.etree.ElementTree as ET

import httpx

from feedscope.fetchers.base import BaseFetcher
from feedscope.models import Article, FetchResult

NS = {"atom": "http://www.w3.org/2005/Atom"}
ARXIV_API = "http://export.arxiv.org/api/query"


class ArxivFetcher(BaseFetcher):
    source = "arxiv"

    async def fetch(self, query: str, limit: int) -> FetchResult:
        try:
            params: dict[str, str | int] = {"search_query": f"all:{query}", "max_results": limit}
            response = await self._client.get(ARXIV_API, params=params, timeout=self._timeout)
            response.raise_for_status()
            root = ET.fromstring(response.text)
            entries = root.findall("atom:entry", NS)
            articles: list[Article] = []
            for entry in entries:
                title = entry.findtext("atom:title", default="", namespaces=NS).strip()
                summary = entry.findtext("atom:summary", default="", namespaces=NS).strip()
                url = entry.findtext("atom:id", default="", namespaces=NS).strip()
                published = entry.findtext("atom:published", default="", namespaces=NS).strip()
                authors = [
                    a.findtext("atom:name", default="", namespaces=NS)
                    for a in entry.findall("atom:author", NS)
                ]
                article = Article(
                    title=title,
                    url=url,
                    source=self.source,
                    published_at=published,
                    authors=authors,
                    summary=summary,
                )
                articles.append(article)
            return FetchResult(source=self.source, articles=articles)
        except httpx.HTTPStatusError as e:
            return FetchResult(source=self.source, error=f"HTTP {e.response.status_code}")
        except httpx.RequestError as e:
            return FetchResult(source=self.source, error=f"Request error: {e}")
        except ET.ParseError as e:
            return FetchResult(source=self.source, error=f"XML parse error: {e}")
