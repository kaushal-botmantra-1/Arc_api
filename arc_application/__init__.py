from flask import Flask
from .config import config_by_name
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

from .services.ageing_api import ageing


def create_app(config_name):
    """this function creates application instance

    Args:
        config_name (string): either dev or prod.

    Returns:
        app : it returns instance of the application
    """
    app = Flask(__name__)
    # adding config object to application
    app.config.from_object(config_by_name[config_name])

    # registering blueprints to main application
    app.register_blueprint(ageing)

    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
