from pymicro_auth.resource.apiv1.user import UserResource
from pymicro_auth.resource.apiv1.auth import AuthResource
from pymicro_auth import api_v1 as api

api.add_resource(
    UserResource,
    "/users",
    methods=['GET', 'POST'],
    endpoint='users'
)

api.add_resource(
    UserResource,
    '/users/<user_id>',
    methods=['GET', 'PATCH', 'DELETE'],
    endpoint='user'
)

api.add_resource(
    AuthResource,
    '/auth/token',
    methods=["POST", "GET"],
    endpoint='auth_token'
)