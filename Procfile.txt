release: python3manage.py migrate
web: gunicorn melhorrotacerto.wsgi --preload --log-file -