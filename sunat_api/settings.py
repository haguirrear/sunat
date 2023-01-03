from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_AUTH_URL: str = "https://api-seguridad.sunat.gob.pe"
    BASE_URL: str = "https://api-cpe.sunat.gob.pe"
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()