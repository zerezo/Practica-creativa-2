#!usr/bin/python3
from subprocess import call
import os
import sys

#------------------------------------------------------------[DEPENDENCIAS]------------------------------------------------------------
call(['sudo', 'apt', 'update'])
call(['sudo', 'apt', 'upgrade'])
call(['sudo', 'apt', 'install', 'docker.io'])

#------------------------------------------------------------[FUNCIONES]------------------------------------------------------------
"""
    Esta función realiza los siguientes pasos:
    1. Construye una imagen Docker etiquetada como 'product-page/18' usando el Dockerfile en el directorio actual.
    2. Ejecuta un contenedor Docker basado en la imagen construida, nombrado 'product-page-p18', 
       mapeando el puerto 9080 del host al puerto 5060 del contenedor, y establece la variable de entorno 
       GROUP_NUMBER a 18.
 """
def crear():
    call(['sudo', 'docker', 'build', '-t', 'product-page/18', '.'])
    os.system('sudo docker run --name product-page-p18 -p 5080:5080 -e GROUP_NUMBER=18 -d product-page/18')

def liberar():
    os.system('sudo docker stop product-page-p18')
    os.system('sudo docker container prune -f')




#------------------------------------------------------------[CODIGO PRINCIPAL]------------------------------------------------------------
param = sys.argv

if param[1] == "crear":
    crear()
elif param[1] == "liberar":
    liberar()
else:
    print("Opción no válida. Use 'crear' o 'liberar'.")
    sys.exit(1)
