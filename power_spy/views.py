from flask import Blueprint, jsonify, render_template

from .update import is_updating, update, update_available

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/update")
def update_page():
    return render_template("update.html")


@views.route("/api/update", methods=["GET"])
def update_check():
    return jsonify({"updatable": update_available()})


@views.route("/api/update", methods=["POST"])
def do_update():
    success = False
    if update_available() and not is_updating():
        update()
        success = True

    return jsonify({"success": success})


@views.route("/api/updating")
def update_status():
    return jsonify({"updating": is_updating()})
