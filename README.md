
## Instalación del proyecto

#### Pararse en la carpeta edmachina, donde se encuentra el docker-compose.yml y correr comando de docker para buildear imagenes de docker
* docker-compose build

#### Para ejecutar los contenedores de backend, frontend y postgres
* docker-compose up -d

#### Ingresar al contenedor backend donde se encuentra en ejecución FastApi
* docker exec -it backend bash

#### Una vez a dentro del contenedor backend, ejecutar el siguiente comando para reflejar las migraciones en la base de datos
* alembic upgrade c42969

#### Luego de eso, ya podremos ingresar a la sigueinte url para interactuar con la aplicación
* http://localhost:3000/



## Documentación de la Api

#### Una vez que los contenedores estén en ejecición, se puede tener acceso a la documentación de los endpoints realizados, ingresando a:
* http://localhost:8000/docs



## Como esta formada la aplicación:
### La aplicacion cuenta con varios apartados de creación de registros y listado de los mismos.

##### * Crear Carrera: Vista para la creación de las carreras
##### * Creacion de Materias: Podemos continuar con la creacion de las materias que estará relacionada a alguna de las carreras creadas previamente.
#### * Creacion de Leads: Un registro para creacion de un lead con los datos personales
#### * Creación de una Inscripción: Para registrar el cursado de materia y carrera de un lead
#### * Lista de Carreras: Listado de los registros de las carreras
#### * Lista de Materias: Vista que muestra las materias disponibles para cursar
#### * Lista de leads: Lista de los leads registados en la base de datos.
#### * Lista de Inscripciones: Lista de los leads que estan inscriptos a una materia/carrera



## Pasos para ingresar a la base de datos del challenge

#### Ingresar al contenedor de postgres
* docker exec -it db bash

#### para ingresar a la base de datos
* psql -U edmachinauser -d edmachinadb


## Pasos que se realizaron para instalar el front
Para el front use React
* npm create vite@latest
* buscamos e instalamos react router dom https://reactrouter.com/en/main
* npm install react-router-dom



## Pasos que se realizaron para instalar alembic (No hace falta correr nuevamente)

#### Agregar alembic a requirements.txt
* alembic==1.12.0

#### Ir al contenedor de backend y ejeutar este comando para generar el folder alembic y alembic.ini
* alembic init alembic

#### IMPORTANTE: para crear migraciones con alembic, debemos importar los modelos en env.py
* User, Lead, Career, Subjects, EnrollmentStudy

#### crear los archivos de migraciones: ingresar al contenedor de backend y ejecutar:
* alembic revision --autogenerate -m "Create first models"

#### Para reflejar las migraciones en la base de datos:
* alembic upgrade c42969

