#### Ir al contenedor de backend y ejeutar este comando para generar el folder alembic y alembic.ini
* alembic init alembic

#### correr migraciones: ingresar al contenedor de backend y ejecutar:
* alembic revision --autogenerate -m "Create first models"

#### Para reflejar las migraciones en la base de datos:
* alembic upgrade e1d373


#### para ingresar a la base de datos
* psql -U edmachinauser -d edmachinadb


#### IMPORTANTE: para crear migraciones con alembic, debemos importar los modelos en env.py
* User, Lead, Career, Subjects, EnrollmentStudy


docker-compose run --rm backend 

docker-compose run --rm --service-port backend alembic revision --autogenerate -m "Create first models"
docker-compose run --rm --service-port backend alembic upgrade e1d373




* npm create vite@latest
* buscamos e instalamos react router dom https://reactrouter.com/en/main
* npm install react-router-domc