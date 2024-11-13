#tabla de muchos
from sqlmodel import Field, Relationship
from app.schemas.libro import LibroBase
from app.models.autor_model import Autor

class Libro(LibroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    autor: Autor | None = Relationship(back_populates="libros")