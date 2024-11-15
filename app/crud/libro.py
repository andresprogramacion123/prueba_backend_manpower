# Importaciones relacionadas con los tipos de datos
from typing import Optional
# Importaciones relacionados son orm sqlmodel y sqlalchemy
from sqlmodel import select
from sqlalchemy.orm import joinedload
# Importacion relacionada con transmitir sesion de base de datos
from app.services._base import AppCRUD
# Importaciones relacionados con modelos y esquemas
from app.models.libro_model import Libro
from app.models.autor_model import Autor
from app.schemas.libro import LibroCreate

####### Capa de acceso a base de datos #######

class LibroCRUD(AppCRUD):
   
   #Crear un libro (Create o Registrar) (Revisado)
#################################################################################################
   def crear_libro(self, libro: LibroCreate) -> Optional[Libro]:
        db_libro = Libro.model_validate(libro)
        self.session.add(db_libro)
        self.session.commit()
        self.session.refresh(db_libro)
        return db_libro
#################################################################################################

   #Mostrar solo un libro de acuerdo a su id (Read by id) (Revisado)
#################################################################################################
   def leer_libro_by_id(self, libro_id: int) -> Optional[Libro]:
      # Seleccionamos el libro que queremos mostrar
      libro = self.session.get(Libro, libro_id)
      return libro
#################################################################################################
   
   #Mostrar solo un libro de acuerdo a su titulo (Read by titulo) (Busqueda) (Revisado)
#################################################################################################
   def busqueda_libro_by_titulo(self, by_titulo: str) -> Libro:
      # Seleccionamos los libros para mostrar
      statement = select(Libro).where(Libro.titulo.ilike(f"%{by_titulo}%"))
      libros = self.session.exec(statement).all()
      return libros
#################################################################################################

   #Mostrar solo un libro de acuerdo a su autor (Read by titulo) (Busqueda) (Revisado)
#################################################################################################
   def busqueda_libro_by_autor(self, by_autor: str) -> Libro:
      # Seleccionamos los libros para mostrar
      statement = (select(Libro).options(joinedload(Libro.autor)).where(Libro.autor.has(Autor.nombre.ilike(f"%{by_autor}%"))))
      libros = self.session.exec(statement).all()
      return libros
#################################################################################################

   #Mostrar libros de acuerdo a su año (Read by año) (Filtro) (Revisado)
#################################################################################################
   def read_libros_by_año(self, by_año: int) -> Libro:
      # Seleccionamos los libros que queremos mostrar
      statement = select(Libro).where(Libro.año_publicacion == by_año)
      libro = self.session.exec(statement).all()
      return libro
#################################################################################################

   #Mostrar libros de acuerdo a su autor (Read by autor) (Filtro) (Revisado)
#################################################################################################
   def read_libros_by_autor(self, autor_nombre: str) -> Libro:
      # Seleccionamos los libros que queremos mostrar
      statement = (select(Libro).options(joinedload(Libro.autor)).where(Libro.autor.has(nombre=autor_nombre)))
      libros = self.session.exec(statement).all()
      return libros
#################################################################################################
     
   #Mostrar todos los libros, con todas las columnas (Read all) (Revisado)
#################################################################################################
   def leer_libro(self) -> Libro:
      libros = self.session.exec(select(Libro)).all()
      return libros
#################################################################################################
   
   #Mostrar todos los libros, pero teniendo en cuenta el offset y limit como parametros de query (Revisado)
#################################################################################################
   def leer_libro_ol(self, offset: int, limit: int) -> Libro:
      libros = self.session.exec(select(Libro).offset(offset).limit(limit)).all()
      return libros
#################################################################################################

   #Eliminar un libro (Delete) (Revisado)
#################################################################################################
   def eliminar_libro_by_id(self, libro: Libro) -> dict: 
      self.session.delete(libro)
      self.session.commit()
      return {"libro eliminado con exito": libro.titulo}
#################################################################################################
   
   #Actualizar algun campo para un libro por su id (Update)
#################################################################################################
   def update_libro_by_id(self, db_libro: Libro) -> Optional[Libro]:
      self.session.add(db_libro)
      self.session.commit()
      self.session.refresh(db_libro)
      return db_libro
#################################################################################################