from functools import wraps
from flask import request, abort
from flask_restx._http import HTTPStatus
from pymicro_auth import Config
from jwt import decode
from jwt.exceptions import ExpiredSignatureError

from pymicro_auth.model import User

function_role_mapper = {
    "get_users": {
        "users": ["admin"]
    },
    "get_user": {
        "users": ["admin", ":user_id"]
    }
}


def auth_required(callback_func):
    @wraps(callback_func)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            abort(HTTPStatus.UNSUPPORTED_MEDIA_TYPE, "supported media types: ['Application/Json']")
        if not Config.JWT_AUTH_TOKEN_HEADER in request.headers:
            abort(HTTPStatus.BAD_REQUEST, "Undefined X-Auth-Token")

        jwt_token = request.headers.get(Config.JWT_AUTH_TOKEN_HEADER)
        try:
            jwt_token_data = decode(jwt_token, Config.JWT_TOKEN_SECRET, algorithms=["HS512"])
        except ExpiredSignatureError:
            abort(HTTPStatus.UNAUTHORIZED, "Token has been expired")
        except:
            abort(HTTPStatus.BAD_REQUEST, "Token is not valid")

        user = User.query.get(jwt_token_data['user_id'])
        if user is None:
            abort(HTTPStatus.NOT_FOUND, "User not exist anymore")

        mapper = function_role_mapper[callback_func.__name__]
        if user.username in mapper['users']:
            return callback_func(*args, **kwargs)

        if ':user_id' in mapper['users']:
            if 'user_id' not in callback_func.__code__.co_varnamses:
                abort(HTTPStatus.FORBIDDEN, "User Doesn't Have rights to access this ressource")
            user_id_mapper = callback_func.__code__.co_varnamses.index('user_id')
            if args[user_id_mapper] == user.id:
                return callback_func(*args, **kwargs)

        abort(HTTPStatus.FORBIDDEN, "User Doesn't Have rights to access this ressource")

    return wrapper
