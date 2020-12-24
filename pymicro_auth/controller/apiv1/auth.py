from time import time

from flask_restx import abort
from flask_restx._http import HTTPStatus
from flask import request

from pymicro_auth import Config
from pymicro_auth.model import User
from pymicro_auth.schema.api.v1 import UserSchema
from jwt import encode, decode
from jwt.exceptions import ExpiredSignatureError

class AuthController:

    @staticmethod
    def generate_token():

        if not request.is_json:
            abort(HTTPStatus.BAD_REQUEST, "data must be json")
        user_schema = UserSchema()
        data = user_schema.load(request.get_json())
        if "username" not in data or "password" not in data:
            abort(HTTPStatus.BAD_REQUEST, 'user and pass required')

        user = User.query.filter_by(username=data['username']).first()
        if user is None:
            abort(HTTPStatus.NOT_FOUND, "User Or Password Wrong")

        if user['password'] != data['password']:
            abort(HTTPStatus.NOT_FOUND, "User Or Password Wrong")

        current_time = time()
        jwt_token = encode(
            {
                'username': user.username,
                'user_id': user.user_id,
                'iss': 'pymicro_auth',  # Issuer
                'iat': current_time,  # Issued At
                'nbf': current_time,  # Not Before
                'exp': current_time + Config.JWT_TOKEN_LIFETIME,  # Expires At
            }
            , Config.JWT_TOKEN_SECRET,
            algorithm=Config.JWT_TOKEN_MAIN_ALGORITHM
        ).decode('utf-8')  # encode generate binary type token with 'b' at first. so we must convert it to utf 8
        user_schema = UserSchema()
        return {'user': user_schema.dump(user)}, HTTPStatus.CREATED, {Config.JWT_SUBJECT_TOKEN_HEADER: jwt_token}

    @staticmethod
    def verify_token():
        if not request.is_json:
            return abort(HTTPStatus.BAD_REQUEST, "data must be json")
        if Config.JWT_SUBJECT_TOKEN_HEADER not in request.headers:
            return abort(HTTPStatus.BAD_REQUEST, "x-subject header not set")
        jwt_token = request.headers.get(Config.JWT_SUBJECT_TOKEN_HEADER)
        try:
            jwt_token_data = decode(
                jwt_token,
                Config.SECRET,
                algorithms=["HS512"]
            )
        except ExpiredSignatureError:
            abort(HTTPStatus.UNAUTHORIZED, 'Token has been expired')
        except:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR)

        user = User.query.get(jwt_token_data['user_id'])
        return user
        if user is None:
            abort(HTTPStatus.NOT_FOUND, 'User Not Found')
        user_schema = UserSchema()
        return {"user": user_schema.dump(user)}, HTTPStatus.OK, {Config.JWT_SUBJECT_TOKEN_HEADER: jwt_token}
