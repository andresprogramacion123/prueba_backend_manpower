from typing import Literal
import secrets
import warnings
from typing_extensions import Self
from pydantic import HttpUrl, PostgresDsn, model_validator, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import MultiHostUrl

class Settings(BaseSettings):
    #Variables de entorno bases de datos
    ECHO: bool = True # Debe ser False en produccion 
    SENTRY_DSN: HttpUrl | None = None
    POSTGRES_SERVER: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = ""
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )
    #Variables de entorno bases de datos
    
    #Variables de entorno backend
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM : str = "HS256"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    DOMAIN: str = "localhost" # Debemos cambiar en produccion
    ENVIRONMENT: Literal["local","production"] = "local"

    @computed_field  # type: ignore[misc]
    @property
    def server_host(self) -> str:
        # Use HTTPS for anything other than local development
        if self.ENVIRONMENT == "local":
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"
    #Variables de entorno backend

    def _check_default_secret(self, var_name: str, value: str | None) -> None:
        if value == "changethis":
            message = (
                f'The value of {var_name} is "changethis", '
                "for security, please change it, at least for deployments."
            )
            if self.ENVIRONMENT == "local":
                warnings.warn(message, stacklevel=1)
            else:
                raise ValueError(message)

    @model_validator(mode="after")
    def _enforce_non_default_secrets(self) -> Self:
        self._check_default_secret("SECRET_KEY", self.SECRET_KEY)
        self._check_default_secret("POSTGRES_PASSWORD", self.POSTGRES_PASSWORD)
        return self
       
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
        )

settings = Settings()