from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

class Settings(BaseSettings):
    path_router: str
    host_db: str
    user_db: str
    password_db: str
    name_db: str
    port_db: int

    class Config:
        env_file = str(ENV_FILE) 
        env_file_encoding = "utf-8"

settings = Settings()