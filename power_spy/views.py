from flask import Blueprint, jsonify, render_template

from .powerspy import is_pc_on, press_power_button
from .update import is_updating, update, update_available

views = Blueprint("views", __name__)
api = Blueprint("api", __name__, url_prefix="/api")


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/update")
def update_page():
    return render_template("update.html")


@api.route("/update", methods=["GET"])
def update_check():
    return jsonify({"updatable": update_available()})


@api.route("/update", methods=["POST"])
def do_update():
    success = False
    if update_available() and not is_updating():
        update()
        success = True

    return jsonify({"success": success})


@api.route("/updating")
def update_status():
    return jsonify({"updating": is_updating()})


@api.route("/power", methods=["GET"])
def power_status():
    return jsonify({"status": is_pc_on()})


@api.route("/power", methods=["POST"])
def power_on():
    if not is_pc_on():
        press_power_button()

    return jsonify({"success": True})


views.register_blueprint(api)
