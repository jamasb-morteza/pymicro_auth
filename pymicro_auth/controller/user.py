from pymicro_auth.model import Users
class UserController:

    @staticmethod
    def get_users():
        return Users

    @staticmethod
    def get_user(user_id):
        return Users[user_id]

    @staticmethod
    def create_user():
        pass