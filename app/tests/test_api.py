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

def test_create_autor(client: TestClient):
    response = client.post(
        "/autor/crear", json={"nombre": "Deadpond", "correo": "Dive Wilson","edad": 34}
    )
    data = response.json()

    assert response.status_code == 201
    assert data["nombre"] == "Deadpond"
    assert data["correo"] == "Dive Wilson"
    assert data["edad"] == 34
    assert data["id"] is not None

def test_leer_autor_by_id(client: TestClient):
    # Crear un autor primero
    response_create = client.post(
        "/autor/crear", json={"nombre": "Autor de Prueba", "correo": "autor@prueba.com", "edad": 45}
    )
    autor_id = response_create.json()["id"]

    # Obtener el autor por ID
    response = client.get(f"/autor/{autor_id}")
    data = response.json()

    assert response.status_code == 200
    assert data["nombre"] == "Autor de Prueba"
    assert data["correo"] == "autor@prueba.com"
    assert data["edad"] == 45

def test_crear_libro(client: TestClient):
    # Crear un autor necesario para el libro
    response_autor = client.post(
        "/autor/crear", json={"nombre": "Autor Libro", "correo": "autorlibro@prueba.com", "edad": 50}
    )
    autor_id = response_autor.json()["id"]

    # Crear un libro asociado al autor
    response = client.post(
        "/libro/crear", 
        json={"titulo": "Libro de Prueba", "año_publicacion": 2021, "isbn": 123456789, "autor_id": autor_id}
    )
    data = response.json()

    assert response.status_code == 201
    assert data["titulo"] == "Libro de Prueba"
    assert data["año_publicacion"] == 2021
    assert data["isbn"] == 123456789
    assert data["autor_id"] == autor_id

def test_leer_libro_by_id(client: TestClient):
    # Crear un autor y un libro primero
    response_autor = client.post(
        "/autor/crear", json={"nombre": "Autor para Libro", "correo": "autorlibro2@prueba.com", "edad": 35}
    )
    autor_id = response_autor.json()["id"]

    response_libro = client.post(
        "/libro/crear", 
        json={"titulo": "Libro Específico", "año_publicacion": 2020, "isbn": 987654321, "autor_id": autor_id}
    )
    libro_id = response_libro.json()["id"]

    # Obtener el libro por ID
    response = client.get(f"/libro/{libro_id}")
    data = response.json()

    assert response.status_code == 200
    assert data["titulo"] == "Libro Específico"
    assert data["año_publicacion"] == 2020
    assert data["isbn"] == 987654321
    assert data["autor_id"] == autor_id

def test_eliminar_libro_by_id(client: TestClient):
    # Crear un autor y un libro primero
    response_autor = client.post(
        "/autor/crear", json={"nombre": "Autor para Borrar", "correo": "borrar@prueba.com", "edad": 45}
    )
    autor_id = response_autor.json()["id"]

    response_libro = client.post(
        "/libro/crear", 
        json={"titulo": "Libro para Borrar", "año_publicacion": 2022, "isbn": 112233445, "autor_id": autor_id}
    )
    libro_id = response_libro.json()["id"]

    # Eliminar el libro por ID
    response = client.delete(f"/libro/eliminar/{libro_id}/")

    assert response.status_code == 202

    # Verificar que el libro ya no existe
    response_check = client.get(f"/libro/{libro_id}")
    assert response_check.status_code == 500