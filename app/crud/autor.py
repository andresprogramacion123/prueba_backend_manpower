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
     