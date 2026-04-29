from abc import ABC, abstractmethod

import httpx

from feedscope.models import FetchResult


class BaseFetcher(ABC):
    def __init__(self, client: httpx.AsyncClient, timeout: float = 30.0) -> None:
        self._client = client
        self._timeout: float = timeout

    @abstractmethod
    async def fetch(self, query: str, limit: int) -> FetchResult: ...
