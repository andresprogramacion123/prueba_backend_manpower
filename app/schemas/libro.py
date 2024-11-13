#tabla de muchos
from typing import Optional
from sqlmodel import SQLModel, Field

class LibroBase(SQLModel):
    titulo: str = Field(index=True,unique=True) #index true para las busquedas
    año_publicacion: int = Field(index=True) #index true para las busquedas
    isbn: int 
    autor_id: int = Field(foreign_key="autor.id")

class LibroCreate(LibroBase):
    pass

class LibroRead(LibroBase):
    id: int
    
class LibroUpdate(SQLModel):
    titulo: str | None = None
    año_publicacion: int | None = None
    isbn: int | None = None
    autor_id: int | None = None

class LibroReadWithAutor(LibroRead):
    autor: "AutorRead"

# Importaciones relacionados con modelos y esquemas
# El codigo siguiente no es elegante, aun asi resuelve el problema de importaciones circulares
from app.schemas.autor import AutorRead
AutorRead.update_forward_refs()