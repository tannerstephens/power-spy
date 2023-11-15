from flask import Flask

from .config import Config
from .views import views


def create_app(config=Config):
    app = Flask(__name__)

    app.config.from_object(config)
    app.register_blueprint(views)

    return app
