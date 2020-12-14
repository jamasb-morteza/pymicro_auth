from pymicro_auth.controller.user import User


class UserResource:
    def get(self, user_id=None):
        """
        :param user_id:
        :return: if user_id set then return user singleton else return user collection
        """
        if (user_id):
            return User.get_user(user_id)
            pass
        else:
            return User.get_users()
            pass
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
