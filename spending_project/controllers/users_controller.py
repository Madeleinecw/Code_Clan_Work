from flask import Blueprint, Flask, redirect, render_template, request

from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# index
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users=users)

# create new user
@users_blueprint.route("/users/new")
def new_user():
    return render_template("users/new.html")

# input page
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    name = request.form["name"]
    new_user = User(name)
    user_repository.save(new_user)
    return render_template("/users/<id>/dashboard.html", user = new_user)

@users_blueprint.route("/users/<id>/dashboard", methods = ["POST"])
def user_dashboard(id):
    user = user_repository.select(id)
    return render_template("/users/dashboard.html", user = user)

@users_blueprint.route("/users/<id>", methods=["POST"])
def update_user(id):
    name = request.form["name"]
    user = User(name, id)
    user_repository.update(user)
    return redirect("/users/dashboard.html")

@users_blueprint.route("/users/dashboard", methods = ["POST"])
def signed_up():
    name = request.form["name"]
    user = User(name, id)
    user_repository.save(user)
    return render_template("/users/first_visit.html", user = user)




