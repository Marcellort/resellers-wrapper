from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    #APIS URLS
    RESSELLERS_API_URL: str = None

settings = Settings(_env_file='.env')