from flask_restx import abort
from flask_restx._http import HTTPStatus
from flask import request
from pymicro_auth.model import User
from pymicro_auth import db
from pymicro_auth.schema.api.v1 import UserSchema


class UserController:

    @staticmethod
    def get_users():
        users = User.query.all()
        user_schema = UserSchema(many=True)
        return {user_schema.dump(users)}

    @staticmethod
    def get_user(user_id):
        user = User.query.get(user_id)
        if user is None:
            abort(HTTPStatus.NOT_FOUND, "User Not Found")

        user_schema = UserSchema()

        return {"user": user_schema.dump(user)}

    @staticmethod
    def create_user():
        user_schema = UserSchema()
        data = user_schema.load(request.get_json())
        if not "username" in data or not "password" in data:
            return abort(HTTPStatus.BAD_REQUEST, "username and password required.")

        user = User.query.filter_by(username=data['username']).first()
        if not user is None:
            return abort(HTTPStatus.BAD_GATEWAY.CONFLICT, "username already taken.")

        user = User(username=data['username'], password=data['password'])
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            return abort(HTTPStatus.INTERNAL_SERVER_ERROR, "Somthing Went Wrong Please Try Again Later")
        return {"user": user_schema.dump(user)}
