from flask import Flask, Blueprint
from flask_restx import Api
from pymicro_auth.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask.cli import AppGroup

db = SQLAlchemy()
marshmallow = Marshmallow()
migrate = Migrate()
api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")
api_v1 = Api(api_v1_bp)

app_cli = AppGroup("app", help="commands")  # point to pymmycro_auth/command/app
from pymicro_auth import command
from pymicro_auth import resource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(api_v1_bp)
    app.cli.add_command(app_cli)
    return app
