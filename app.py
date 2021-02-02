import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/all_plants")
def all_plants():
    plants = list(mongo.db.plants.find())
    return render_template("plants.html", plants=plants)


@app.route("/register", methods=("GET", "POST"))
def register():

    if request.method == "POST":
        # check to see if username exists already in mongo db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username already exists")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        if password != confirm_password:
            flash("Passwords did not match! Please try again.")
            return redirect(url_for("register"))

        if password == confirm_password:
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"), method="pbkdf2:sha256:8000")
            }

        mongo.db.users.insert_one(register)

        # enter new user into cookie 'session'
        session["user"] = request.form.get("username").lower()
        flash("Congratulations, you are now registered!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in mongo db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome {}".format(
                        request.form.get("username").capitalize()))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # incorrect password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesnt exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the username from mongo db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # delete session cookies for user
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    if request.method == "POST":
        plant = {
            "name": request.form.get("name"),
            "botanical_name": request.form.get("botanical_name"),
            "description": request.form.get("description"),
            "watering": request.form.get("watering"),
            "size": request.form.get("size"),
            "light_needed": request.form.get("light_needed"),
            "room": request.form.get("room"),
            "img_url": request.form.get("img_url"),
            "created_by": session["user"]
        }
        mongo.db.plants.insert_one(plant)
        flash("Plant Added")
        return redirect(url_for("all_plants"))

    return render_template("add_plant.html")


@app.route("/edit<plant_id>", methods=["GET", "POST"])
def edit(plant_id):
    plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    return render_template("edit.html", plant=plant)


@app.route("/delete<plant_id>")
def delete(plant_id):
    mongo.db.plants.remove({"_id": ObjectId(plant_id)})
    flash("Plant Deleted")
    return redirect(url_for("all_plants"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
