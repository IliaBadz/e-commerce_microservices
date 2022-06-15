import os

from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    GRPC_SERVER_ADDRESS: str = os.getenv('GRPC_SERVER_ADDRESS')


@lru_cache()
def get_settings() -> Settings:
    return Settings()
