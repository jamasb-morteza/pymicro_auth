from pymicro_auth import db
from pymicro_shared_libraries import generate_uuid


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True, default=generate_uuid)
    username = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password = db.Column(db.String(128), nullable=True)
