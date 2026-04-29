import json

import httpx

from feedscope.fetchers.base import BaseFetcher
from feedscope.models import Article, FetchResult

HN_API = "https://hn.algolia.com/api/v1/search"
HN_THREAD_URL = "https://news.ycombinator.com/item"  # use for url null fallback

class HNFetcher(BaseFetcher):
    async def fetch(self, query: str, limit: int) -> FetchResult:
        try:
            params: dict[str, str | int] = {
                "tags": "story",
                "query": query,
                "hitsPerPage": limit,
            }
            response = await self._client.get(HN_API, params=params, timeout=self._timeout)
            response.raise_for_status()
            data = response.json()
            hits = data["hits"]
            articles: list[Article] = []
            for hit in hits:
                hit_url = hit.get("url")
                if not hit_url:
                    hit_url = f"{HN_THREAD_URL}?id={hit['objectID']}"
                article = Article(
                    title=hit["title"].strip(),
                    url=hit_url,
                    source="hn",
                    published_at=hit["created_at_i"],
                    authors=[hit["author"]],
                    summary="",
                )
                articles.append(article)
            return FetchResult(source="hn", articles=articles)
        except httpx.HTTPStatusError as e:
            return FetchResult(source="hn", error=f"HTTP {e.response.status_code}")
        except httpx.RequestError as e:
            return FetchResult(source="hn", error=f"Request error: {e}")
        except json.JSONDecodeError as e:
            return FetchResult(source="hn", error=f"JSON parse error: {e}")
