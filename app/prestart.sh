#! /usr/bin/env bash

# Deja que la DB comience

echo "##### Hola, este es un mensaje desde el script bash para ver que esta corriendo.####"
echo "##### A continuacion vamos a ejecutar el script de python. Para verificar conexion con base de datos ####"

python /app/app/database/session.py

echo "##### El script python se ejecuto correctamente ####"

#Luego podemos crear data inicial en caso de ser necesario