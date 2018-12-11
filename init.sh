#!/bin/sh
export PGPASSWORD='alumnodb'
#A rellenar: escribir alumnodb siempre
dropdb -U alumnodb exampsi
createdb -U alumnodb exampsi

python manage.py makemigrations exam
python manage.py migrate

python manage.py createsuperuser

python populate.py
