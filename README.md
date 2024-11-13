# Prueba técnica desarrollador backend python 

**Julian Andres Montoya Carvajal C.C 1214727927**

## Parte 1: Instrucciones de instalacion y ejecucion

* Preferiblemente tener instalado Ubuntu 22.04.3 LTS (Jammy) (Windows tambien se puede pero debe poder instalar docker y docker compose).

* Asegurate de instalar Docker version 24.0.7 y ademas Docker Compose version 2.21.0. El siguiente link te puede ayudar a obtener los dos https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04

* Clone el repositorio con los siguientes comandos (debe tener instalado git)

```bash
git clone https://github.com/andresprogramacion123/prueba_backend_manpower.git
```

* Ingresa a la carpeta donde esta el proyecto

```bash
cd andresprogramacion123/prueba_backend_manpower
```

* Crea el archivo .env con las variables de entorno correspondientes, para tener un ejemplo puede ver el archivo adjunto en el proyecto llamado .env_example

* Posteriomente ejecute el archivo docker-compose.yml para ejecutar el proyecto

```bash
sudo docker compose up --build
```

* Visita http://localhost:5000/ en tu navegador para acceder a la aplicacion

* Visita http://localhost:5000/docs en tu navegador para acceder a la documentación interactiva de la API generada automáticamente por FastAPI.

* Visita http://localhost:5050/ en tu navegador para acceder a la interfaz grafica de la base de datos postgresql.

**Nota:** En caso de tener problemas con puertos ya utilizados, ejecutar comando siguiente para conocer el ID del contenedor

```bash
sudo docker ps
```

Luego detener el contenedor con el siguiente comando

```bash
sudo docker stop ID_CONTENEDOR
```

## Parte 2: Estructura del proyecto y esquema relacional

## Parte 3: Preguntas adicionales

7) ejecutar pruebas unitarias con pytest:

```bash
export PYTHONDONTWRITEBYTECODE=1 && pytest
```

7) generar covertura y reporte de cobertura:

```bash
export PYTHONDONTWRITEBYTECODE=1 && coverage run -m pytest
```

```bash
export PYTHONDONTWRITEBYTECODE=1 && coverage report
```

```bash
export PYTHONDONTWRITEBYTECODE=1 && coverage html
```