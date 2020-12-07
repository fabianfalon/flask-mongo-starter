# Microservicios
Ejemplo de aplicación en flask y mongo.


### 1 Run with docker
    $ docker-compose build
    $ docker-compose up


#### Run without docker
    $ virtualenv venv --python=/usr/bin/python3.8
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py runserver