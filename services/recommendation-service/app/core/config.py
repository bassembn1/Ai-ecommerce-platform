from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    RABBITMQ_HOST: str
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str 
    RABBITMQ_PASSWORD: str 

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    QDRANT_HOST: str
    QDRANT_PORT: int
    QDRANT_COLLECTION: str

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
print("RABBITMQ_HOST =", settings.RABBITMQ_HOST)
print("RABBITMQ_PORT =", settings.RABBITMQ_PORT)
print("DATABASE =", settings.POSTGRES_DB)
print("HOST =", settings.POSTGRES_HOST)