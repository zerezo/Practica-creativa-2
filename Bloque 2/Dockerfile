# Imagen base
FROM python:3.7.7-slim

# Clonar el repo de github
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git

# Instalar dependencias
RUN pip install -r /practica_creativa2/bookinfo/src/productpage/requirements.txt


# Exponer el puerto para la aplicación
EXPOSE 5080

# Pasar la variable de entorno al contenedor
ENV GROUP_NUM=""

# Comando para ejecutar la aplicación
CMD ["python", "/practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "5080"]