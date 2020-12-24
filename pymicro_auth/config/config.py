from os import environ


class Config:
    DEBUG = bool(environ.get("PYMICRO_AUTH_DEBUG", False))
    TESTING = bool(environ.get("PYMICRO_AUTH_TESTING", False))
    ENV = environ.get("PYMICRO_AUTH_ENV", "production")

    SQLALCHEMY_DATABASE_URI = environ.get("PYMICRO_AUTH_SQL_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
    JWT_TOKEN_SECRET = environ.get('PYMICRO_JWT_TOKEN_SECTRET', '1*2?>X.3$45x6w7r8t9')
    JWT_TOKEN_LIFETIME = int(environ.get('PYMICRO_JWT_TOKEN_LIFETIME', 100))
    JWT_TOKEN_MAIN_ALGORITHM = environ.get('PYMICRO_JWT_ALGORITHM', 'HS512')

    JWT_SUBJECT_TOKEN_HEADER = 'X-Subject-Token'
    JWT_AUTH_TOKEN_HEADER = 'X-Auth-Token'