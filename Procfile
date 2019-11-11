release: python PaginaPersonalAlexV1/manage.py flush --noinput ;  python PaginaPersonalAlexV1/manage.py migrate

web: sh -c 'cd PaginaPersonalAlexV1 && gunicorn PaginaPersonalAlexV1.wsgi --log-file -'

