#tabla de uno
from app.schemas.autor import AutorBase
from sqlmodel import Field, Relationship

class Autor(AutorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    libros: list["Libro"] = Relationship(back_populates="autor")