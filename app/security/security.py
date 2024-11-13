# Importamos tipo de datos para retorno de funciones
from typing import Any
# Importamos tipos de datos de fecha
from datetime import datetime, timedelta

# Importamos JWT
from jose import jwt
# Importamos passlib para encryptar contraseñas
from passlib.context import CryptContext

# Importamos variables de entorno
from app.config.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Funcion de seguridad para hashear contraseñas en base de datos
#################################################################################################
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
#################################################################################################

# Funcion de seguridad encargada de verificar la contraseña para la autenticacion (signin) de un usuario
#################################################################################################
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
#################################################################################################

# Funcion de seguridad encargada de generar un nuevo token de acceso
#################################################################################################
def create_access_token(subject: str|Any, expires_delta: timedelta = None) -> str:

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes = 15) # Modificar con VARIABLE DE ENTORNO de  ACCESS_TOKEN_EXPIRE_MINUTES ¿?

    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode,  settings.SECRET_KEY, algorithm = settings.ALGORITHM)

    return encoded_jwt
#################################################################################################