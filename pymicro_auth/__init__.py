from flask import Flask, Blueprint
from flask_restx import Api
from pymicro_auth.config import Config

apiv1_bp = Blueprint('apiv1', __name__, url_prefix='/api/v1')
apiv1 = Api(apiv1_bp)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(apiv1_bp)
    return app
