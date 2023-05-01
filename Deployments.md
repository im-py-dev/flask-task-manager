## (Waitress)
`waitress-serve --host 0.0.0.0 --port 80 --call wsgi:create_app`

`wsgi.py`

```
from app import app as application

def create_app():
    return application
```

<hr>

## (gunicorn)
`gunicorn -w 4 wsgi:create_app -b 0.0.0.0:8000`


`wsgi.py`

```
from app import app as application

def create_app():
    return application
```


<hr>

## (uwsgi)
`uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app --processes 5`


`wsgi.py`

```
from app import app
```
