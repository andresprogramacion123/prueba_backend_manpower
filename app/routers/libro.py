# Importacion de framework fastapi
from fastapi import APIRouter, Query, Depends, status
# Importacion de servicios de logica y crud
from app.services.libro import LibroService
# Importacion relacionada con dependencias
from app.dependencies import get_session
# Importaciones relacionados son orm sqlmodel y sqlalchemy
from sqlmodel import Session 
# Importaciones relacionados con modelos y esquemas
from app.schemas.libro import LibroCreate, LibroRead, LibroUpdate, LibroReadWithAutor # Esquemas
# Importamos controlador de resultados
from app.utils.service_result import handle_result

router = APIRouter()

#Endpoint Crear libro (Create libro)
#Posee excepciones personalizadas
########################################################################################################################
@router.post(
    "/libro/crear"
    ,response_model=LibroRead
    ,status_code=status.HTTP_201_CREATED
    ,tags=["Libros"]
    )
async def crear_libro(
    *
    ,session: Session = Depends(get_session)
    ,libro: LibroCreate
    ):
    '''
    Crear libro
    '''
    result = LibroService(session).crear_libro(libro)

    return handle_result(result)
########################################################################################################################

#Endpoint Mostrar solo un libro de acuerdo a su id (Read by id)
#(Posee excepciones personalizadas)
########################################################################################################################
@router.get(
    "/libro/{libro_id}"
    ,response_model=LibroReadWithAutor
    ,status_code=status.HTTP_200_OK
    ,tags=["Libros"]
    )
async def leer_libro_by_id(
    *
    ,session: Session = Depends(get_session)
    ,libro_id: int
    ):
    '''
    Leer libro by id
    '''
    result = LibroService(session).leer_libro_by_id(libro_id)

    return handle_result(result)
########################################################################################################################

#Endpoint Mostrar todos los libros con su autor con busqueda por titulo, con todas las columnas (Read all) 
#(Posee excepciones personalizadas)
########################################################################################################################
@router.get(
    "/libro/todos/search/titulo"
    ,response_model=list[LibroReadWithAutor]
    ,status_code=status.HTTP_200_OK
    ,tags=["Busqueda Libros"]
    )
async def busqueda_libro_by_titulo(
    *
    ,session: Session = Depends(get_session)
    ,titulo : str
    ):
    '''
    Leer todos los libros buscados por titulo
    '''
    result = LibroService(session).busqueda_libro_by_titulo(titulo)

    return handle_result(result)
########################################################################################################################

#Endpoint Mostrar todos los libros con su autor con busqueda por autor, con todas las columnas (Read all) 
#(Posee excepciones personalizadas)
########################################################################################################################
@router.get(
    "/libro/todos/search/autor"
    ,response_model=list[LibroReadWithAutor]
    ,status_code=status.HTTP_200_OK
    ,tags=["Busqueda Libros"]
    )
async def busqueda_libro_by_autor(
    *
    ,session: Session = Depends(get_session)
    ,autor : str
    ):
    '''
    Leer todos los libros buscados por autor
    '''
    result = LibroService(session).busqueda_libro_by_autor(autor)

    return handle_result(result)
########################################################################################################################

#Endpoint Mostrar todos los libros con su autor filtrados por año, con todas las columnas (Read all) 
#(Posee excepciones personalizadas)
########################################################################################################################
@router.get(
    "/libro/todos/año/"
    ,response_model=list[LibroReadWithAutor]
    ,status_code=status.HTTP_200_OK
    ,tags=["Libros"]
    )
async def read_libros_by_año(
    *
    ,session: Session = Depends(get_session)
    ,año : int
    ):
    '''
    Leer todos los libros filtrados por año
    '''
    result = LibroService(session).read_libros_by_año(año)

    return handle_result(result)
########################################################################################################################

#Endpoint Mostrar todos los libros con su autor filtrados por autor, con todas las columnas (Read all) 
#(Posee excepciones personalizadas)
########################################################################################################################
@router.get(
    "/libro/todos/autor/"
    ,response_model=list[LibroReadWithAutor]
    ,status_code=status.HTTP_200_OK
    ,tags=["Libros"]
    )
async def read_libros_by_autor(
    *
    ,session: Session = Depends(get_session)
    ,autor : str
    ):
    '''
    Leer todos los libros filtrados por autor
    '''
    result = LibroService(session).read_libros_by_autor(autor)

    return handle_result(result)
########################################################################################################################

#Endpoint Mostrar todos los libros con su autor, con todas las columnas (Read all) 
#(Posee excepciones personalizadas)
########################################################################################################################
@router.get(
    "/libro/all/"
    ,response_model=list[LibroReadWithAutor]
    ,status_code=status.HTTP_200_OK
    ,tags=["Libros"]
    )
async def leer_libro(
    *
    ,session: Session = Depends(get_session)
    ):
    '''
    Leer todos los libros
    '''
    result = LibroService(session).leer_libro()

    return handle_result(result)
########################################################################################################################

#Endpoint Mostrar todos los libros, pero teniendo en cuenta el offset y limit como parametros de query para paginacion
#(Posee excepciones personalizadas)
########################################################################################################################
@router.get(
    "/libros/all-o-l"
    ,response_model=list[LibroReadWithAutor]
    ,status_code=status.HTTP_200_OK
    ,tags=["Libros"]
    )
async def leer_libro_ol(
    *
    ,session: Session = Depends(get_session)
    ,offset: int = Query(default=0)
    ,limit: int = Query(default=100, lte=100)
    ):
    '''
    Leer todos los libros con todas sus columnas pero con limit and offset
    '''
    result = LibroService(session).leer_libro_ol(offset,limit)

    return handle_result(result)
########################################################################################################################

#Endpoint Eliminar un libro by id (Delete by id)
#(Posee excepciones personalizadas)
########################################################################################################################
@router.delete(
    "/libro/eliminar/{libro_id}/"
    ,status_code=status.HTTP_202_ACCEPTED
    ,tags=["Libros"]
    )
async def eliminar_libro_by_id(
    *
    ,session: Session = Depends(get_session)
    ,libro_id: int
    ):
    '''
    Eliminar un libro a partir de su id
    '''
    result = LibroService(session).eliminar_libro_by_id(libro_id)

    return handle_result(result)
########################################################################################################################

#Actualizar algun campo para un libro por su id (Update)
########################################################################################################################
@router.patch(
    "/libro/{libro_id}"
    ,response_model=LibroReadWithAutor
    ,status_code=status.HTTP_200_OK
    ,tags=["Libros"]
    )
async def update_libro_by_id(
    *
    ,session: Session = Depends(get_session)
    ,libro_id: int
    ,libro: LibroUpdate
    ):

    result = LibroService(session).update_libro_by_id(libro_id, libro)

    return handle_result(result)
########################################################################################################################'''

