# Importacion relacionada con transmitir sesion de base de datos
from app.services._base import AppService
# Importacion relacionada con CRUD del servicio
from app.crud.autor import AutorCRUD
# Importaciones relacionados con modelos y esquemas
from app.schemas.autor import AutorCreate
# Funcion de utilidad para todos los servicios
from app.utils.service_result import ServiceResult
from app.utils.exceptions import AppException

####### Capa de logica de los servicios #######

class AutorService(AppService):
       
    #Crear un autor (Create o Registrar) (Posee excepciones personalizadas)
#################################################################################################
    def crear_autor(self, autor: AutorCreate) -> ServiceResult:
        
        #Verificamos que el autor no se encuentre creado
        autor_in_db = AutorCRUD(self.session).read_autor_by_nombre(autor.nombre)
        
        if autor_in_db:
            return ServiceResult(AppException.ReadAutor({
                "Nombre": autor.nombre
                ,"Detalle":"El nombre del autor ya se encuentra registrado"
            }))
        
        db_autor = AutorCRUD(self.session).crear_autor(autor)
        
        if not db_autor:
            return ServiceResult(AppException.CreateAutor({
                "Detalle":"No se pudo crear el autor, por favor verifique los datos ingresados"
            }))
                    
        return ServiceResult(db_autor)
#################################################################################################

#Mostrar solo un autor de acuerdo a su id (Read by id) (Posee excepciones personalizadas)
#################################################################################################
    def leer_autor_by_id(self, autor_id: int) -> ServiceResult:
        
        autor = AutorCRUD(self.session).leer_autor_by_id(autor_id)
        
        if not autor:
            return ServiceResult(AppException.ReadAutor({
                "Identificador": autor_id
                ,"Detalle":"El identificador del autor no se encuentra"
            }))
            
        return ServiceResult(autor)
#################################################################################################