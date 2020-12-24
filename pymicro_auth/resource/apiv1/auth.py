from flask_restx import Resource

from pymicro_auth.controller.apiv1 import AuthController


class AuthResource(Resource):
    def get(self):
        return AuthController.verify_token()

    def post(self):
        return AuthController.generate_token()
