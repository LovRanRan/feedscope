from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from feedscope.config import FetchConfig
from feedscope.models import Article


def test_article_rejects_empty_title() -> None:
    with pytest.raises(ValidationError):
        Article.model_validate(
            {
                "title": "",
                "url": "https://example.com",
                "source": "arxiv",
                "published_at": datetime(2024, 8, 15, tzinfo=UTC),
            }
        )


def test_article_parses_unix_timestamp() -> None:
    article = Article.model_validate(
        {
            "title": "test",
            "url": "https://example.com",
            "source": "arxiv",
            "published_at": 1723737138,
        }
    )
    assert article.published_at == datetime(2024, 8, 15, 15, 52, 18, tzinfo=UTC)


def test_fetch_config_reads_env_var(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FEEDSCOPE_QUERY", "ai")
    config = FetchConfig() # type: ignore
    assert config.query == "ai"
