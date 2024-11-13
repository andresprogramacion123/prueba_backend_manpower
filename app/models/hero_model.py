#tabla de muchos
from sqlmodel import Field, Relationship
from app.schemas.hero import HeroBase

class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)