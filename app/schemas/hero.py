#tabla de muchos
from typing import Optional
from sqlmodel import SQLModel, Field

class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

class HeroCreate(HeroBase):
    pass

class HeroPublic(HeroBase):
    id: int
    
class HeroUpdate(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None
    team_id: int | None = None