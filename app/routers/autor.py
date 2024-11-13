# Importacion de framework fastapi
from fastapi import APIRouter, Query, Depends, status
# Importacion de servicios de logica y crud
from app.services.autor import AutorService
# Importacion relacionada con dependencias
from app.dependencies import get_session
# Importaciones relacionados son orm sqlmodel y sqlalchemy
from sqlmodel import Session 
# Importaciones relacionados con modelos y esquemas
from app.schemas.autor import AutorCreate, AutorRead, AutorReadWithLibro # Esquemas
# Importamos controlador de resultados
from app.utils.service_result import handle_result

router = APIRouter()

#Endpoint Crear autor (Create autor)
#Posee excepciones personalizadas
########################################################################################################################
@router.post(
    "/autor/crear"
    ,response_model=AutorRead
    ,status_code=status.HTTP_201_CREATED
    ,tags=["Autores"]
    )
async def crear_autor(
    *
    ,session: Session = Depends(get_session)
    ,autor: AutorCreate
    ):
    '''
    Crear autor
    '''
    result = AutorService(session).crear_autor(autor)

    return handle_result(result)
########################################################################################################################

#Endpoint Mostrar solo un autor de acuerdo a su id (Read by id)
#(Posee excepciones personalizadas
########################################################################################################################
@router.get(
    "/autor/{autor_id}"
    ,response_model=AutorRead
    ,status_code=status.HTTP_200_OK
    ,tags=["Autores"]
    )
async def leer_autor_by_id(
    *
    ,session: Session = Depends(get_session)
    ,autor_id: int
    ):
    '''
    Leer autor by id
    '''
    result = AutorService(session).leer_autor_by_id(autor_id)

    return handle_result(result)
########################################################################################################################
