import os

from flask import Flask

from src.exceptions import APIException
from src.helpers import mongo
from src.views import BLUEPRINT as api
from mongoengine import *

connect('system_manager', host='localhost', port=27017) # connect without mongo
# connect with mongo
"""username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
host = os.getenv("MONGO_HOST")
port = os.getenv("MONGO_PORT")
connect(
    os.getenv("MONGO_DATABASE"),
    host=f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
)"""


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    app.config["MONGO_DBNAME"] = "system_manager"
    app.config["MONGO_URI"] = "mongodb://localhost:27017/system_manager"
    app.config["SECRET_KEY"] = "PB3aGvTmCkzaLGRAxDc3aMayKTPTDd5usT8gw4pCmKOk5AlJjh12pTrnNgQyOHCH"

    mongo.init_app(app)
    # register blueprints
    app.register_blueprint(api)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {
            "app": app,
        }

    return app
