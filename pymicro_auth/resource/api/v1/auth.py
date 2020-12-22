from flask_restx import Resource

from pymicro_auth.controller.api.v1 import AuthController


class AuthResource(Resource):
    @staticmethod
    def get():
        return AuthController.verify_token()

    @staticmethod
    def post():
        return AuthController.generate_token()
