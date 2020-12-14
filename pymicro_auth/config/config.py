from os import environ


class Config:
    DEBUG = bool(environ.get('PYMICRO_AUTH_DEBUG', False))
    ENV = bool(environ.get('PYMICRO_AUTH_ENV', 'production'))
    TESTING =  environ.get('PYMICRO_AUTH_TESTING', False)
