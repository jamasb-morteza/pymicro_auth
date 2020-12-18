from flask import Flask, Blueprint
from flask_restx import Api
from pymicro_auth.config import Config
api_v1_bp =Blueprint("api_v1", __name__, url_prefix="/api/v1")
api_v1 = Api(api_v1_bp)
from pymicro_auth import resource
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api_v1_bp)
    return app