from pymicro_auth import marshmallow
from pymicro_auth.model import User


class UserSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = User

    id = marshmallow.auto_field(dump_only=True)
    username = marshmallow.auto_field()
    password = marshmallow.auto_field()
