# Proyecto template 2024. 

**Desarrollado por Julian Andres Montoya Carvajal (julianmontoya3.1416@gmail.com)**

Esta es proyecto plantilla utilizando el framework FastAPI 💪 y el ORM SQLModel 💪💪

Para conocer la documentacion del framework visite https://fastapi.tiangolo.com/ y https://sqlmodel.tiangolo.com/

## Iniciar proyecto de desarrollo local desde cero

1) 

a) Instalar Ubuntu (particionando el disco):

    Preferiblemente tener instalado Ubuntu 22.04.3 LTS (Jammy) 
    (Falta documentación)

b) Instalar ubuntu en windows con wsl:
    
    (Falta documentación)

2) Instalar python (Superior a 3.10):

Preferiblemente tener instalado Python version 3.10.12
(Falta documentación)

3) Instalar pip (administrador de paquetes):

(Falta documentación)

4) Establecer entorno virtual:

(Falta documentación)

```bash
virtualenv env --python=python3
```

5) Activa el entorno virtual en linux:

```bash
source env/bin/activate
```

6) Instalar dependencias y asignarlas en requirements.txt

```bash
pip install fastapi
pip install sqlmodel
pip install psycopg2-binary (controlador para db postgresql)
pip install tenacity (para conexion con db)
pip install pydantic-settings (para variables de entorno)
pip install "passlib[bcrypt]" (para la seguridad)
pip install "python-jose[cryptography]" (para la seguridad)
pip install emails (para envio de emails)
pip install weasyprint (para generacion de pdfs)
pip install pytest (para pruebas unitarias)
pip install alembic (para migraciones)
```

```bash
python -m pip freeze > requirements.txt 
```