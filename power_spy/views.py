from flask import Blueprint, jsonify, redirect, render_template, request, session

from .login import check_password
from .powerspy import is_pc_on, press_power_button
from .update import is_updating, update, update_available

views = Blueprint("views", __name__)
api = Blueprint("api", __name__, url_prefix="/api")


def logged_in():
    return session.get("logged_in", False)


@views.route("/")
def home():
    if logged_in():
        return render_template("home.html")
    return redirect("/login")


@views.route("/update")
def update_page():
    if logged_in():
        return render_template("update.html")
    return redirect("/login")


@views.route("/login")
def login():
    return render_template("login.html")


@api.route("/update", methods=["GET"])
def update_check():
    if logged_in():
        return jsonify({"success": True, "updatable": update_available()})
    return jsonify({"success": False})


@api.route("/update", methods=["POST"])
def do_update():
    success = False
    if logged_in():
        if update_available() and not is_updating():
            update()
            success = True

    return jsonify({"success": success})


@api.route("/updating")
def update_status():
    if logged_in():
        return jsonify({"success": True, "updating": is_updating()})

    return jsonify({"success": False})


@api.route("/power", methods=["GET"])
def power_status():
    if logged_in():
        return jsonify({"status": is_pc_on()})

    return jsonify({"success": False})


@api.route("/power", methods=["POST"])
def power_on():
    success = False
    if logged_in():
        if not is_pc_on():
            success = True
            press_power_button()

    return jsonify({"success": success})


@api.route("/login", methods=["POST"])
def api_login():
    password = request.json["password"]

    success = False
    if check_password(password):
        success = True
        session["logged_in"] = True

    return jsonify({"success": success})

@api.route("/reboot", methods=["GET"])
def reboot():
    if logged_in():
        

views.register_blueprint(api)
