# Importaciones relacionadas con los tipos de datos
from typing import Optional
# Importaciones relacionados son orm sqlmodel y sqlalchemy
from sqlmodel import select
# Importacion relacionada con transmitir sesion de base de datos
from app.services._base import AppCRUD
# Importaciones relacionados con modelos y esquemas
from app.models.autor_model import Autor
from app.schemas.autor import AutorCreate

####### Capa de acceso a base de datos #######

class AutorCRUD(AppCRUD):
   
   #Crear un autor (Create o Registrar)
#################################################################################################
   def crear_autor(self, autor: AutorCreate) -> Optional[Autor]:
        db_autor = Autor.model_validate(autor)
        self.session.add(db_autor)
        self.session.commit()
        self.session.refresh(db_autor)
        return db_autor
#################################################################################################

   #Mostrar solo un autor de acuerdo a su id (Read by id)
#################################################################################################
   def leer_autor_by_id(self, autor_id: int) -> Optional[Autor]:
      # Seleccionamos el autor que queremos mostrar
      autor = self.session.get(Autor, autor_id)
      return autor
#################################################################################################
   
   #Mostrar solo un autor de acuerdo a su nombre (Read by nombre)
#################################################################################################
   def read_autor_by_nombre(self, by_nombre: str) -> Optional[Autor]:
      # Seleccionamos el autor que queremos mostrar
      statement = select(Autor).where(Autor.nombre == by_nombre)
      autor = self.session.exec(statement).first()
      return autor
#################################################################################################
     
   #Mostrar todos los autores, con todas las columnas (Read all)
#################################################################################################
   def autores_leer(self) -> Autor:
      autores = self.session.exec(select(Autor)).all()
      return autores
#################################################################################################
   
   #Mostrar todos los autores, pero teniendo en cuenta el offset y limit como parametros de query
#################################################################################################
   def autores_leer_ol(self, offset: int, limit: int) -> Autor:
      autores = self.session.exec(select(Autor).offset(offset).limit(limit)).all()
      return autores
#################################################################################################

   #Eliminar un autor (Delete)
#################################################################################################
   def eliminar_autor_by_id(self, autor: Autor) -> dict: 
      self.session.delete(autor)
      self.session.commit()
      return {"autor eliminado con exito": autor.nombre}
#################################################################################################
   
   #Actualizar algun campo para un autor por su id (Update)
#################################################################################################
   def update_autor_by_id(self, db_autor: Autor) -> Optional[Autor]:
      self.session.add(db_autor)
      self.session.commit()
      self.session.refresh(db_autor)
      return db_autor
#################################################################################################