from subprocess import call
import os, sys

def arrancar(port_param = '9080'):
    call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])
    call(['sudo', 'apt-get', 'update'])
    call(['sudo', 'apt-get', 'install', '-y', 'python3-pip'])
    os.chdir('practica_creativa2/bookinfo/src/productpage')

    call(['pip3', 'install', '-r', 'requirements.txt'])

    os.environ['GROUP_NUMBER'] = '18'

    # Ruta al archivo de la plantilla
    template_file_path = 'templates/productpage.html'

    # Nuevo título
    new_title = os.getenv('GROUP_NUMBER', 'Grupo')

    # Actualizar el título de la plantilla
    update_template_title(template_file_path, new_title)

    call(['python3', 'productpage_monolith.py', port_param])

def liberar():
    call(['rm', '-rf', 'practica_creativa2'])

def update_template_title(file_path, new_title):
    try:
        # Leer el contenido del archivo
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Abrir el archivo en modo escritura para modificarlo
        with open(file_path, 'w') as file:
            for line in lines:
                # Reemplazar el bloque title cuando se encuentre
                if '{% block title %}' in line:
                    file.write(f'{{% block title %}}{new_title}{{% endblock %}}\n')
                else:
                    file.write(line)



        # Imprimir un mensaje de éxito
        print(f"El título de la plantilla se ha actualizado correctamente a '{new_title}'.")
    except IOError:
        # Imprimir un mensaje de error si ocurre un problema al modificar el archivo
        print("Error al modificar el archivo de configuración.")
        sys.exit(1)

param = sys.argv

if param[1] == "arrancarPuerto":
    arrancar(param[2])

if param[1] == "arrancar":
    arrancar()

if param[1] == "liberar":
    liberar()