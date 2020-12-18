from pymicro_auth.resource.api.v1.user import UserResource
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
