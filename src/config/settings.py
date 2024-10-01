from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "UniTrade API"

    class Config:
        case_sensitive = True
