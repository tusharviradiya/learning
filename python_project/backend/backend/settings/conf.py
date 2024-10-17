from goodconf import GoodConf
from pydantic import Field


class AppConfig(GoodConf):

    "Database configuration"
    PG_DB_HOST: str = Field(initial="localhost", description="Postgres port")
    PG_DB_PORT: int = Field(initial=5432, description="Postgres port")
    PG_DB_USER: str = Field(initial="app", description="Postgres port")
    PG_DB_PASS: str = Field(initial="", description="Postgres port")
    PG_DB_NAME: str = Field(initial="app", description="Postgres port")

config = AppConfig()
