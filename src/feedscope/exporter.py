import json
from pathlib import Path

from feedscope.models import FetchResult


def write_json(results: list[FetchResult], path: Path) -> None:
    data = [r.model_dump(mode="json") for r in results]
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
