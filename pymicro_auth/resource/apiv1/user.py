from flask_restx import Resource
from pymicro_auth.controller.apiv1 import UserController

class UserResource(Resource):

    def get(self, user_id=None):
        """
        :arg user_id
        :returns user singleton / users collection
        """
        if user_id is None:
            return UserController.get_users()

        return UserController.get_user(int(user_id))

    def post(self):
        return UserController.create_user()
        pass

    def patch(self):
        pass

    def delete(self):
        pass
