from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "UniTrade API"
    OPENAI_API_KEY: str

    class Config:
        case_sensitive = True
