import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool  # Para base de datos en memoria
#Importamos todos los modelos
from app.models.autor_model import Autor
from app.models.libro_model import Libro
from app.dependencies import get_session

from app.main import app

client = TestClient(app)

#######################################################################
@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
#######################################################################

'''def test_create_autor(client: TestClient):
    response = client.post(
        "/autor/crear", json={"nombre": "Deadpond", "correo": "Dive Wilson","edad": 34}
    )
    data = response.json()

    assert response.status_code == 201
    assert data["nombre"] == "Deadpond"
    assert data["correo"] == "Dive Wilson"
    assert data["edad"] == 34
    assert data["id"] is not None

def test_create_libro(client: TestClient):
    response = client.post(
        "/libro/crear", json={"titulo": "Deadpond", "año_publicacion": "2003","isbn": 34}
    )
    data = response.json()

    assert response.status_code == 201
    assert data["titulo"] == "Deadpond"
    assert data["año_publicacion"] == "2003"
    assert data["isbn"] == 34
    assert data["autor_id"] is not None
    assert data["id"] is not None'''