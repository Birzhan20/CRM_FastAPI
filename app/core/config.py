from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'CRM'
    DATABASE_URL: str = 'sqlite+aiosqlite:///crm.db'
    SECRET_KEY: str = ''
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        env_file = '.env'


settings = Settings()
