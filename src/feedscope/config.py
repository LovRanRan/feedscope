from pathlib import Path
from typing import Annotated

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from feedscope.models import SourceName


class FetchConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="FEEDSCOPE_", env_file=".env", extra="ignore")
    query: Annotated[str, Field(min_length=1)]
    limit: Annotated[int, Field(gt=0, le=100)] = 20
    sources: list[SourceName] = ["arxiv", "hn"]
    output_path: Path | None = None
