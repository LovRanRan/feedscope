from abc import ABC, abstractmethod
from typing import ClassVar

import httpx

from feedscope.models import FetchResult, SourceName


class BaseFetcher(ABC):
    source: ClassVar[SourceName]

    def __init__(self, client: httpx.AsyncClient, timeout: float = 30.0) -> None:
        self._client = client
        self._timeout: float = timeout

    @abstractmethod
    async def fetch(self, query: str, limit: int) -> FetchResult: ...
