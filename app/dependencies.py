from collections.abc import Generator
from sqlmodel import Session
# Importamos motor de base de datos
from app.database.session import engine

# Dependencia de base de datos
#################################################################################################
def get_session() -> Generator[Session,None, None]:
    with Session(engine) as session:
        yield session
#################################################################################################