from flask import Blueprint, Flask, redirect, render_template, request

from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# INDEX
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users=users)

@users_blueprint.route("/users/new")
def new_user():
    return render_template("users/new.html")

@users_blueprint.route("/users", methods=["POST"])
def create_user():
    name = request.form["name"]
    new_user = User(name)
    user_repository.save(new_user)
    return redirect("/users")