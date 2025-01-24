# Practica-creativa-2
Practica creativa 2 de la asignatura de CDPS, en la que se implementará el despliegue de servicios de varias maneras, desde monoliticamente hasta GKE


Esta práctica tiene como objetivo diseñar e implementar un escenario completo de despliegue de una aplicación fiable y escalable, integrando diversas tecnologías estudiadas a lo largo de la asignatura. Este proyecto permite consolidar los conocimientos adquiridos en temas clave como el despliegue de aplicaciones en la nube y arquitecturas basadas en microservicios, utilizando herramientas modernas como Docker y Kubernetes. 


Para ello, se definen cuatro grandes bloques y uno opcional.
Despliegue de una aplicación monolítica en una máquina virtual pesada
Despliegue de una aplicación monolítica usando docker.
Segmentación de una aplicación monolítica en microservicios utilizando docker-compose.
Despliegue de una aplicación basada en microservicios utilizando Kubernetes.
Despliegue de la infraestructura completa de práctica usando Helm Charts (opcional)

Despliegue de la aplicación en máquina virtual pesada 

En este primer escenario se realizará el despliegue de la aplicación en una máquina virtual utilizando la infraestructura de Google Cloud, seleccionada por su fiabilidad y escalabilidad. El proceso comienza con la creación de una instancia de máquina virtual configurada con las especificaciones necesarias para soportar la aplicación. Se establece además una regla de firewall que permite todo tipo de tráfico, garantizando la conectividad requerida. 
Una vez creada la máquina virtual, se procede a cargar el script desarrollado para la gestión del ciclo de vida de la aplicación. Para iniciar la aplicación se ejecuta el comando 
python3 bloque1.py arrancar
lo que permite que la aplicación se ejecute de forma predeterminada en la IP externa de la máquina en el puerto 9080. Si se desea utilizar un puerto diferente, es posible especificarlo en el momento de iniciar la aplicación mediante el comando 	python3 bloque1.py arrancarPuerto PUERTO
donde "PUERTO" será sustituido por el número del puerto deseado. Para finalizar el proceso y liberar los recursos utilizados en la máquina virtual, se debe ejecutar el comando 
python3 bloque1.py liberar 
asegurando así una gestión eficiente del entorno.



Despliegue de una aplicación monolítica usando docker 

Se utiliza una instancia de máquina virtual en Google Cloud para desplegar una aplicación monolítica mediante Docker. En este caso, se configura un único servicio dentro de la instancia asignada al escenario 1. El proceso incluye la creación de un archivo Dockerfile, que define todos los pasos necesarios para construir y ejecutar el contenedor. Este archivo especifica la imagen base que se utilizará, los comandos necesarios para clonar los repositorios requeridos, la exposición del puerto, que por defecto será el 9080, y el comando que se ejecutará al iniciar el contenedor.
Además, el script correspondiente a este bloque automatiza el proceso de creación y ejecución del contenedor. A partir del Dockerfile, se genera una imagen que servirá como base para iniciar el contenedor, el cual se nombra como "product-page-p18".
Para iniciar la aplicación, simplemente se debe ejecutar el comando 
python3 bloque2.py crear
lo que pone en marcha la aplicación en el puerto 9080. 
Una vez que se desee liberar los recursos utilizados, se puede ejecutar el comando	
 python3 bloque2.py liberar
 asegurando así una gestión eficiente de los recursos.
Segmentación de una aplicación monolítica en microservicios utilizando docker-compose 
En este tercer bloque, se continuará trabajando con una instancia de máquina virtual en Google Cloud, configurando las reglas de firewall correspondientes (FW) para permitir el acceso adecuado. El objetivo principal es segmentar la aplicación monolítica en varios microservicios utilizando docker-compose, implementando una arquitectura orientada a microservicios.


Se procederá a crear los archivos Dockerfile para cada uno de los servicios que conforman la aplicación: ProductPage, Details, Ratings y Reviews. Cada archivo contendrá las instrucciones necesarias para construir la imagen del microservicio correspondiente, respetando las especificaciones técnicas, como la elección de la imagen base, las rutas de archivos, las variables de entorno, la exposición de puertos y los comandos de ejecución específicos.


Además, se generará un archivo docker-compose.yml que permitirá el despliegue de los contenedores creados para cada servicio. Este archivo definirá las variables de entorno necesarias para garantizar que los microservicios funcionen correctamente.
El script principal de este bloque, denominado bloque3.py, será desarrollado en Python para automatizar el despliegue de la aplicación. Al ejecutar el comando python3 bloque3.py, el script se encargará de construir las imágenes, levantar los contenedores correspondientes y asegurar que la aplicación sea accesible a través del puerto 9080 en la IP externa de la máquina virtual.
Las principales diferencias al usar Docker para una aplicación monolítica frente a una segmentada en microservicios radican en la arquitectura, escalabilidad y mantenimiento. En un modelo monolítico, toda la aplicación se ejecuta en un único contenedor, lo que simplifica el despliegue inicial, pero dificulta el mantenimiento, ya que cualquier cambio requiere reconstruir y desplegar todo el sistema. Además, la escalabilidad es limitada, ya que se debe replicar el contenedor completo, consumiendo más recursos.
En cambio, al usar microservicios con Docker Compose, cada servicio funciona de manera independiente en su propio contenedor, permitiendo desarrollarlos, actualizarlos y escalarlos de forma individual. Esto mejora la eficiencia, ya que se pueden escalar solo los servicios necesarios, y facilita el mantenimiento gracias a la modularidad y el desacoplamiento.

Para ejecutar el script que iniciará la aplicación en el puerto 9080 de la IP externa de la máquina virtual, utilizaremos el comando: 
python3 bloque3.py.

Despliegue de una aplicación basada en microservicios utilizando Kubernetes 

En este escenario, se utilizará Kubernetes, una plataforma de código abierto ampliamente utilizada para la gestión de contenedores. Dentro de Google Cloud, se configurará un clúster de Kubernetes Engine (GKE) para desplegar la aplicación.
El proceso comienza iniciando sesión en Google Cloud Platform y configurando el entorno de trabajo mediante la selección del proyecto y la zona correspondiente. Para ello, se ejecutarán los siguientes comandos: gcloud auth login, seguido de gcloud config set project [PROJECT_ID] y gcloud config set compute/zone europe-west1-b.
Una vez configurado el entorno, se procederá a crear el clúster de Kubernetes utilizando el comando gcloud container clusters get-credentials my-cluster --zone europe-west1-b. Esto permitirá establecer la conexión entre el clúster y el entorno local para su gestión.
Para llevar a cabo el despliegue, se aplicarán las definiciones de despliegue y servicios especificadas en archivos YAML individuales. Esto se realizará utilizando el comando kubectl apply -f <nombre-del-archivo>.yaml. Por ejemplo, para desplegar el servicio de Ratings, se empleará el comando:
kubectl apply -f ratings.yaml
De manera similar, las distintas versiones del servicio Reviews se desplegarán aplicando los archivos correspondientes con el formato kubectl apply -f review-<version>-<tipo>.yaml. A continuación, un ejemplo de los comandos de despliegue que se usarían para implementar los servicios principales:
	kubectl apply -f productpage.yaml
	kubectl apply -f details.yaml
	kubectl apply -f ratings.yaml
	kubectl apply -f reviews-svc.yaml
	kubectl apply -f reviews-v3-deployment.yaml

Tras completar el despliegue, se verificará que los servicios y pods se hayan cargado correctamente en el clúster utilizando comandos como kubectl get nodes y kubectl get pods. Finalmente, la aplicación estará operativa y accesible a través del puerto 9080. Para identificar la IP externa y el puerto asignado al servicio ProductPage, se ejecutará el comando kubectl get service productpage-external.

El despliegue de la infraestructura completa de la práctica se realizará utilizando Helm Charts en Google Kubernetes Engine (GKE), que incluye Helm preinstalado para facilitar la gestión y despliegue de aplicaciones en Kubernetes. Para comenzar, se creará un nuevo proyecto de Helm con el comando helm create <nombre_del_proyecto>. Esto generará automáticamente los directorios y archivos necesarios, como Charts, chart.yaml, templates y values.yaml.
A continuación, se copiarán los archivos .yaml de la aplicación en la carpeta templates y se editará el archivo values.yaml para definir desde qué repositorio se descargará la imagen de cada servicio y el puerto en el que se ejecutará. Este proceso permitirá lanzar la aplicación directamente en Kubernetes, habilitándola para que sea accesible externamente a través de la IP asignada por el balanceador de carga.
Para identificar la IP externa, se utilizará el comando kubectl get services. Finalmente, la aplicación será accesible desde cualquier navegador web ingresando en la URL http://<IP_externa>:<puerto>. Este enfoque asegura un despliegue eficiente y una gestión centralizada de los recursos mediante Helm.
Al crear los pods en Kubernetes, se observan varias ventajas en comparación con otros enfoques. Los pods permiten gestionar cada microservicio de forma centralizada mediante archivos YAML, lo que garantiza consistencia y automatización. Además, cada pod ejecuta un único contenedor, lo que fomenta el aislamiento entre servicios y permite una gestión eficiente de los recursos al definir límites de CPU y memoria. Este enfoque declarativo facilita la repetición del despliegue sin depender de configuraciones manuales.
En cuanto a la escalabilidad, esta solución ofrece un control más granular, permitiendo escalar solo los microservicios necesarios ajustando el número de réplicas de cada pod. Por ejemplo, se configuran tres réplicas para el servicio Details y dos para Ratings, optimizando recursos según la demanda. Además, Kubernetes distribuye las réplicas en diferentes nodos, asegurando alta disponibilidad y tolerancia a fallos. A diferencia de una arquitectura monolítica o no orquestada, escalar en Kubernetes resulta más eficiente, ya que no se replican partes innecesarias de la aplicación.


Alejandro Cerezo Gilarranz
Sergio Gutierrez Fernández
Patricia Rodríguez Casado


