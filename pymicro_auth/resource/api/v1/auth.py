from flask_restx import Resource

from pymicro_auth.controller.api.v1 import AuthController


class AuthResource(Resource):
    @staticmethod
    def get():
        AuthController.verify_token()

    @staticmethod
    def post(self):
        AuthController.generate_token()
