from os import environ
class Config:
    DEBUG = bool(environ.get("PYMICRO_AUTH_DEBUG", False))
    TESTING = bool(environ.get("PYMICRO_AUTH_TESTING", False))
    ENV = environ.get("PYMICRO_AUTH_ENV", "production")

    SQLALCHEMY_DATABASE_URI = environ.get("PYMICRO_AUTH_SQL_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
