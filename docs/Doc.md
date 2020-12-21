#### Create Python Virtual Environment:

```bash
virtualenv --python "C:\Program Files\Python39\python.exe" venv
```



#### packages

- Basics
  - flask 
  - simplejson
  - python-dotenv
  - flask-restx

- Database
  - PyMySQL
  - SQLAlchemy
  - Flask-SQLAlchemy
  - marshmallow # ORM: map json object to Python and serializing Python Object //  hide or expose Model data fields
  - marshmallow-sqlalchemy
  - flask-marshmallow
  - Flask-Migrate




- pymicro-shared-libraries



#### Configs Class:

```py
from os import environ

class Config:
    DEBUG = bool(environ.get("PYMICRO_AUTH_DEBUG", False))
    TESTING = bool(environ.get("PYMICRO_AUTH_TESTING", False))
    ENV = environ.get("PYMICRO_AUTH_ENV", "production")

    SQLALCHEMY_DATABASE_URI = environ.get("PYMICRO_AUTH_SQL_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
```



#### Adding Resource Endpoint To API:

```python
from pymicro_auth.resource.api.v1.user import UserResource
from pymicro_auth import api_v1 as api

# Collection Resource
api.add_resource(
    UserResource,
    "/users",
    methods=['GET', 'POST'],
    endpoint='users'
)

# Singleton Resource
api.add_resource(
    UserResource,
    '/users/<user_id>',
    methods=['GET', 'PATCH', 'DELETE'],
    endpoint='user'
)
```

#### Resource Class:

```python
from flask_restx import Resource
class UserResource(Resource):

    def get(self, user_id=None):
        if user_id is None:
			#Do Somthing
			pass
        else:
        	#Do Something Else

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
```



#### Define Model:

```python
from pymicro_auth import db
from pymicro_shared_libraries import generate_uuid


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True, default=generate_uuid)
    username = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password = db.Column(db.String(128), nullable=True)
```



#### Docker Running Mysql Container:

```bash
 docker run -d --rm --name mysql_pymicro_auth -p 3306:3306
 -e MYSQL_ROOT_PASSWORD=123456
 -e MYSQL_DATABASE=pymicro_auth 
 -e MYSQL_USER=pymicro 
 -e MYSQL_PASSWORD=123456 
 mysql
```

```bash
docker container ls
```

```bash
docker inspect mysql_pymicro_auth
```

```bash
docker exec -it mysql_pymicro_auth mysql -u pymicro -p
```



Export Connection String to environment variables For SQLALCHEMY_DATABASE_URI variable:

linux:

```bash
export PYMICRO_AUTH_SQL_URI=mysql+pymysql://<username>:<password>@<host>:<port>/<dbname>
```

windows:

```bash
SET PYMICRO_AUTH_SQL_URI=mysql+pymysql://<username>:<password>@<host>:<port>/<dbname>
```

flask creating migration:

```bash
flask db migrate -m"migration_name"
```

running migration

```bash
flask db upgrade
```

marshmallow: Serializing Python Object to JSON and vice versa

marshmallow-sqlalchemy: Serializing sql object to json

```python
from flask_marshmallow import Marshmallow
var_marshmallow = Marshmallow()

var_marshmallow.init_app(app)
```



Marshmallow Schema:

```python
from ..... import var_marshmallow
```

