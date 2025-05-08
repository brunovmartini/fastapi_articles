from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Setttings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://bruno:admin@localhost:5432/faculdade'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = '79yhs4-Gos51KNTfCjpWimUEtvLZ3gynQm2rZGyiDO8'  # segredo da API
    """
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # token valido por 1 semana (em minutos)

    class Config:
        case_sensitive = True


settings: Setttings = Setttings()
