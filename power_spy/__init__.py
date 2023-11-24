from flask import Flask

from .config import Config
from .login import create_password_file
from .views import views


def create_app(config=Config):
    app = Flask(__name__)

    app.config.from_object(config)
    app.register_blueprint(views)

    create_password_file()

    return app
