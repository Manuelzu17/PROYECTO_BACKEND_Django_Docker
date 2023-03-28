# Title from project

# PASO 1 CREAR Dockerfile

```
FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /my_app_django_dir
WORKDIR /my_app_django_dir
ADD requirements.txt /my_app_django_dir/
# RUN pip install -- upgrade pip && pip install -r requirements.
txt
RUN pip install -r requirements.txt
ADD . /my_app_django_dir/
```
# PASO 2 CREAR docker-compose.yml
```
version: '3.5'
services:
  proyecto_backend:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/my_app_django_dir
    ports:
      - "80:8000"
```

# PASO 3 CREAR PROYECTO
```
sudo docker-compose run proyecto_backend django-admin startproject backend_proyect .
sudo docker-compose run --rm proyecto_backend django-admin startproject backend_proyect .
```
# PASO  4 SUBIR
``` 
docker-compose up
```
# SUBIR DOCKER Y QUE QUEDE EN SEGUNDO
```
docker-compose up -d
```
# SI AGREGO ALGO EN requirements.txt DEBO HACER UN BUILD
```
docker-compose build
```
# realizar migrations
```
sudo docker-compose run --rm proyecto_backend python manage.py makemigrations
```
# realizar migrations
```
sudo docker-compose run --rm proyecto_backend python manage.py migrate
```
# CREAR SUPER USUARIO
```
sudo docker-compose run --rm proyecto_backend python manage.py createsuperuser
```
# CREAR APP
```
sudo docker-compose run --rm proyecto_backend python manage.py startapp erp
```
# EJECTUAR PRUEBAS DESDE EL ARCHIVO DE TESTS.PY PARA CADA APP
```
sudo docker-compose run --rm proyecto_backend python manage.py test app/erp
```
# Ejecutar PRUEBAS DESDE EL ARCHIVO PRINCIPAL DE LAS APPs
```
sudo docker-compose run --rm proyecto_backend python manage.py test app
```
