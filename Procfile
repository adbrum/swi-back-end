web: gunicorn swi.wsgi
releaser: python manage.py makemigrations users --noinput
releaser: python manage.py makemigrations urlimages --noinput
releaser: python manage.py migrate --noinput