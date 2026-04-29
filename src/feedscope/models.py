from datetime import UTC, datetime
from typing import Annotated, Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, HttpUrl

SourceName = Literal["arxiv", "hn"]


class Article(BaseModel):
    model_config = ConfigDict(frozen=True)
    title: Annotated[str, Field(min_length=1)]
    url: HttpUrl
    source: SourceName
    published_at: AwareDatetime
    authors: list[str] | None = None
    summary: str = ""


class FetchResult(BaseModel):
    model_config = ConfigDict(frozen=True)
    source: SourceName
    articles: list[Article] = Field(default_factory=list)
    fetched_at: AwareDatetime = Field(default_factory=lambda: datetime.now(UTC))
    error: str | None = None
