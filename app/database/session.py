from sqlmodel import SQLModel, create_engine, Session, select
from sqlalchemy import Engine
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
import logging
#Importamos todos los modelos, en caso de que no se ejecuten migraciones
from app.models import autor_model, libro_model
from app.config.config import settings

#Motor(Engine) de base de datos: maneja la comunicacion con la base de datos, normalmente solo se tiene un engine para toda la aplicacion y reutilizarlo en todas partes.
###################################################
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=bool(settings.ECHO))

def function_create_tables(): 
    print("Vamos a crear tablas")
    SQLModel.metadata.create_all(engine)
###################################################

#backend_pre_start
######################################################################################################
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1

@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init(db_engine: Engine) -> None:
    try:
        with Session(db_engine) as session:
            # Try to create session to check if DB is awake
            session.exec(select(1))
    except Exception as e:
        logger.error(e)
        raise e

def main() -> None:  
    logger.info("Iniciando servicio")
    init(engine)
    function_create_tables()
    logger.info("Servicio terminado de inicializarse")
######################################################################################################
#backend_pre_start

#bloque principal
if __name__ == "__main__":
    main()