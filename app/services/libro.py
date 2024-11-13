# Importacion relacionada con transmitir sesion de base de datos
from app.services._base import AppService
# Importacion relacionada con CRUD del servicio
from app.crud.libro import LibroCRUD
from app.crud.autor import AutorCRUD
# Importaciones relacionados con modelos y esquemas
from app.schemas.libro import LibroCreate, LibroUpdate
# Funcion de utilidad para todos los servicios
from app.utils.service_result import ServiceResult
from app.utils.exceptions import AppException

####### Capa de logica de los servicios #######

class PlanEstudioService(AppService):
       
    #Crear un libro (Create o Registrar) (Posee excepciones personalizadas)
#################################################################################################
    def crear_libro(self, libro: LibroCreate) -> ServiceResult:
        
        #Verificamos que el autor si se encuentre creado
        autor = AutorCRUD(self.session).leer_autor_by_id(libro.autor_id)
        
        if not autor:
            return ServiceResult(AppException.ReadAutor({
                "Identificador": libro.autor_id
                ,"Detalle":"El identificador del autor no se encuentra"
            }))
        
        db_libro = LibroCRUD(self.session).crear_libro(libro)
        
        if not db_libro:
            return ServiceResult(AppException.CreateLibro({
                "Detalle":"No se pudo crear el libro, por favor verifique los datos ingresados"
            }))
                    
        return ServiceResult(db_libro)
#################################################################################################
    
    #Mostrar todos los libros con todas las columnas (Read all) (Posee excepciones personalizadas)
#################################################################################################
    def leer_libro(self) -> ServiceResult:
        
        libros = LibroCRUD(self.session).leer_libro()

        if not libros:
            return ServiceResult(AppException.ReadLibros({
                "Detalle":"No se pudo obtener todos los libros"
                }))
        
        return ServiceResult(libros)
#################################################################################################

    #Mostrar todos los libros con todas las columnas pero teniendo en cuenta el offset y limit como parametros de query (Read all) (Posee excepciones personalizadas)
#################################################################################################
    def leer_libro_ol(self, offset: int, limit: int) -> ServiceResult:
        
        libros = LibroCRUD(self.session).leer_libro_ol(offset, limit)

        if not libros:
            return ServiceResult(AppException.ReadLibros({
                "Detalle":"No se pudo obtener todos los libros"
                }))
        
        return ServiceResult(libros)
#################################################################################################
    
    #Mostrar solo un libro de acuerdo a su id (Read by id) (Posee excepciones personalizadas)
#################################################################################################
    def leer_libro_by_id(self, libro_id: int) -> ServiceResult:
        
        libro = LibroCRUD(self.session).leer_libro_by_id(libro_id)
        
        if not libro:
            return ServiceResult(AppException.ReadLibro({
                "Identificador": libro_id
                ,"Detalle":"El identificador del libro no se encuentra"
            }))
            
        return ServiceResult(libro)
#################################################################################################

    #Mostrar todos los planes de estudio de acuerdo al id de programa academico (Read by id_programa_academico) (Posee excepciones personalizadas)
#################################################################################################
    def leer_plan_estudio_by_id_programa_academico(self, programa_academico_id: int) -> ServiceResult:
        
        #Verificamos que el programa academico si se encuentre creado
        programa_academico = ProgramaAcademicoCRUD(self.session).leer_programa_academico_by_id(programa_academico_id)
        
        if not programa_academico:
            return ServiceResult(AppException.ReadProgramaAcademico({
                "Identificador": programa_academico_id
                ,"Detalle":"El identificador del programa academico no se encuentra"
            }))
            
        #Filtramos todos los planes de estudio por id de programa academico
        planes_estudio=PlanEstudioCRUD(self.session).read_plan_estudio_by_id_programa(programa_academico_id)
        
        if not planes_estudio:
            return ServiceResult(AppException.ReadPlanesEstudio({
                "Detalle":"No se pudo obtener todos los planes de estudio"
                }))
            
        return ServiceResult(planes_estudio)
#################################################################################################

    #Eliminar un libro (Delete) (Posee excepciones personalizadas)
#################################################################################################
    def eliminar_libro_by_id(self, libro_id: int) -> ServiceResult:
        
        # Seleccionamos el libro a ser eliminado
        libro = LibroCRUD(self.session).eliminar_libro_by_id(libro_id)
        
        if not libro:
            return ServiceResult(AppException.ReadLibro({
                "Identificador": libro_id
                ,"Detalle":"El identificador del libro no se encuentra"
            }))
        
        mensaje = LibroCRUD(self.session).eliminar_libro_by_id(libro)
        
        if not mensaje:
            return ServiceResult(AppException.DeleteLibro({
                "Detalle":"No se pudo eliminar el libro"
            }))
        
        return ServiceResult(mensaje)
#################################################################################################
    
    #Actualizar algun campo para un libro por su id (Update by id)
#################################################################################################
    def update_libro_by_id(self, libro_id: int, libro: LibroUpdate) -> ServiceResult:
        
        # Seleccionamos el plan de estudio a ser actualizado
        db_plan_estudio = PlanEstudioCRUD(self.session).read_plan_estudio_by_id(plan_estudio_id)
        
        if not db_plan_estudio:
            return ServiceResult(AppException.ReadUserby_id({
                "Identificador": plan_estudio_id
                ,"Detalle":"El identificador del plan de estudio no se encuentra"
            }))
            
        # Realizamos cambios
        plan_estudio_data = plan_estudio.dict(exclude_unset=True)
        for key, value in plan_estudio_data.items():
            setattr(db_plan_estudio, key, value)
            
        plan_estudio_update = PlanEstudioCRUD(self.session).update_plan_estudio_by_id(db_plan_estudio)
        
        return ServiceResult(plan_estudio_update)
#################################################################################################