# Importaciones relacionados son orm sqlmodel y sqlalchemy para session
from sqlmodel import Session

class DBSession:
    def __init__(self, session : Session):
        self.session = session

class AppService(DBSession):
    pass

class AppCRUD(DBSession):
    pass