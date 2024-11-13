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

class LibroService(AppService):
       
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

    #Mostrar todos los libros con todas las columnas filtrados por titulo (Read all) (Posee excepciones personalizadas)
    # (Busqueda)
#################################################################################################
    def busqueda_libro_by_titulo(self, titulo: str) -> ServiceResult:
        
        libros = LibroCRUD(self.session).busqueda_libro_by_titulo(titulo)

        if not libros:
            return ServiceResult(AppException.ReadLibros({
                "Detalle":"No se pudo obtener todos los libros"
                }))
        
        return ServiceResult(libros)
#################################################################################################

    #Mostrar todos los libros con todas las columnas filtrados por autor (Read all) (Posee excepciones personalizadas)
    # (Busqueda)
#################################################################################################
    def busqueda_libro_by_autor(self, autor: str) -> ServiceResult:
        
        libros = LibroCRUD(self.session).busqueda_libro_by_autor(autor)

        if not libros:
            return ServiceResult(AppException.ReadLibros({
                "Detalle":"No se pudo obtener todos los libros"
                }))
        
        return ServiceResult(libros)
#################################################################################################

    #Mostrar todos los libros con todas las columnas filtrados por año (Read all) (Posee excepciones personalizadas)
    #(Filtro)
#################################################################################################
    def read_libros_by_año(self, año:int) -> ServiceResult:
        
        libros = LibroCRUD(self.session).read_libros_by_año(año)

        if not libros:
            return ServiceResult(AppException.ReadLibros({
                "Detalle":"No se pudo obtener todos los libros"
                }))
        
        return ServiceResult(libros)
#################################################################################################

    #Mostrar todos los libros con todas las columnas filtrados por autor (Read all) (Posee excepciones personalizadas)
    #(Filtro)
#################################################################################################
    def read_libros_by_autor(self, autor:str) -> ServiceResult:
        
        libros = LibroCRUD(self.session).read_libros_by_autor(autor)

        if not libros:
            return ServiceResult(AppException.ReadLibros({
                "Detalle":"No se pudo obtener todos los libros,verifique que el autor si tenga asignado libros"
                }))
        
        return ServiceResult(libros)
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
    
    #Eliminar un libro (Delete) (Posee excepciones personalizadas)
#################################################################################################
    def eliminar_libro_by_id(self, libro_id: int) -> ServiceResult:
        
        # Seleccionamos el libro a ser eliminado
        libro = LibroCRUD(self.session).leer_libro_by_id(libro_id)
        
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
        
        # Seleccionamos el libro a ser actualizado
        db_libro = LibroCRUD(self.session).leer_libro_by_id(libro_id)
        
        if not db_libro:
            return ServiceResult(AppException.ReadLibro({
                "Identificador": libro_id
                ,"Detalle":"El identificador del libro no se encuentra"
            }))
            
        # Realizamos cambios
        libro_data = libro.dict(exclude_unset=True)
        for key, value in libro_data.items():
            setattr(db_libro, key, value)
            
        libro_update = LibroCRUD(self.session).update_libro_by_id(db_libro)
        
        return ServiceResult(libro_update)
#################################################################################################