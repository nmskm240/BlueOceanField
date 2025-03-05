from dataclasses import dataclass
from pathlib import Path

from sqlalchemy import URL, make_url
import yaml


@dataclass(frozen=True)
class Config:
    logging: dict
    database_url: URL

    @classmethod
    def from_file(cls, path: Path) -> "Config":
        config = {}
        with path.open() as f:
            config = dict(yaml.safe_load(f))
        logging = config.get("logging")
        database_url = config.get("database")["url"]
        return Config(logging=logging, database_url=make_url(database_url))
