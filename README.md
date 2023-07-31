# user_modernizacion_superset_grupo18

## Desplegar localmente Superset
1. Clonar el repositorio de superset que contiene los ajustes realizados
git clone 
2. 
```shell
git clone https://github.com/Arthur-Ackernman/superset
```

2. Lanzar la aplicacion usando docker compouse
moverse a la carpeta de superset
cd superset
Ejecute el siguiente comando
docker-compose -f docker-compos.yml pull
docker-compose -f docker-compose.yml up
Una vez tenga los servicios arriba proceda a subir el servicio de usuarios para poder realizar la autenticación
## Como ejecutar localmente el micro de usuarios
1. Asegurarse de tener Docker y docker-compose instalado. Si actualmente no lo tiene instalado dirigirse
   a la pagina de docker para las intrucciones de instalación de su sistema operativo
2. Ubicarse sobre este directorio y ejecutar docker-compose

```shell
docker-compose up --build
```
## Como ejecutar localmente un servicio
1. Situarse en el servicio a utilizar (publicaciones, usuarios...)
2. Crear y activar entorno virtual env
3. Instalar dependencias
3. Subir servicio

```shell
cd ./users/
python3 -m venv ./
source ./venv/Scripts/activate
pip install -r requirements.txt
python wsgi.py
```

## Como desplegar la aplicación en GCP
1. Repositorios privados con las imagenes de contenedor del microservicio users en Container Registry.
2. gcloud SDK para acceder a los servicios del proveedor Google Cloud Platform a partir de la consola. En caso de no tenerla instalada puede consultar el siguiente manual de instalación: https://cloud.google.com/sdk/docs/install
3. Herramienta de control de Kubernetes, kubectl. En caso de no tenerla instalada puede consultar el siguiente manual de instalación:https://kubernetes.io/es/docs/tasks/tools/install-kubectl/

``` shell
cd ./deployment/
kubectl apply -f secrets.yaml
kubectl apply -f k8s-base-layer-deployment.yaml
kubectl apply -f k8s-new-services-deployment.yaml
kubectl apply -f k8s-ingress-deployments.yaml
```