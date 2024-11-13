#tabla de uno
from sqlmodel import SQLModel, Field

class AutorBase(SQLModel):
    nombre: str = Field(index=True)
    correo: str = Field(index=True, unique=True) #unico
    edad: int

class AutorCreate(AutorBase):
    pass

class AutorRead(AutorBase):
    id: int

class AutorUpdate(SQLModel):
    nombre: str | None = None
    correo: str | None = None
    edad: int | None = None

class AutorReadWithLibro(AutorRead):
    libros: list["LibroRead"] = []

# Importaciones relacionados con modelos y esquemas
# El codigo siguiente no es elegante, aun asi resuelve el problema de importaciones circulares
from app.schemas.libro import LibroRead
LibroRead.update_forward_refs()