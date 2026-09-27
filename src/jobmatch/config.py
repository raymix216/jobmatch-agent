"""Runtime configuration. Everything via env vars prefixed with JOBMATCH_."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="JOBMATCH_")

    app_name: str = "jobmatch-agent"
    log_level: str = "INFO"

    # M1: database_url, redis_url
    # M2: router_model_small, router_model_large, eval_dataset_path


settings = Settings()
