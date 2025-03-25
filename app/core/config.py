from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Configuración obligatoria
    DATABASE_URL: str = "postgresql://user:password@localhost/dbname"
    SECRET_KEY: str = "tu-clave-secreta-jwt"
    ALGORITHM: str = "HS256"
    
    # Configuración opcional con valores por defecto
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MERCADOPAGO_ACCESS_TOKEN: str | None = None
    EMAIL_HOST: str | None = None
    EMAIL_PORT: int | None = None
    EMAIL_USER: str | None = None
    EMAIL_PASSWORD: str | None = None
    EMAIL_FROM_NAME: str | None = None
    ENVIRONMENT: str = "development"
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignora variables no definidas

settings = Settings()