from flask import Flask

from .update import check_for_update, update


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def page():
        return str(check_for_update())

    @app.route("/update")
    def doIt():
        update()

        return "updating"

    @app.route("/test")
    def test():
        return "test"

    return app
