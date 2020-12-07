import os
from flask import Flask
from src.helpers import mongo
from src.exceptions import APIException
from src.views import BLUEPRINT as api

# instantiate the extensions


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    app.config["MONGO_DBNAME"] = "system_manager"
    app.config["MONGO_URI"] = "mongodb://localhost:27017/system_manager"
    # set up extensions

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
