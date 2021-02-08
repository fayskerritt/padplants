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


@app.route("/plants")
def plants():

    """
        Pulls plant data from database depending on search parameters
        input by user in search form.

        Return: displays matching plants from db in plants.html.

    """

    plants = []
    query_params = []
    # find input values from form
    search = request.args.get("search")
    room = request.args.get("room")
    size = request.args.get("size")
    light = request.args.get("light")
    water = request.args.get("water")

    # check to see if each search input has a value
    if search:
        query_params.append({"$text": {'$search': search}})

    if room:
        query_params.append({"room": room})

    if size:
        query_params.append({"size": size})

    if light:
        query_params.append({"light_needed": "Shade"})

    if water:
        query_params.append({"watering": "10-14"})

    if len(query_params) > 0:
        query = {"$and": query_params}
        plants = list(mongo.db.plants.find(query))
    else:
        plants = list(mongo.db.plants.find().sort("_id", -1))

    return render_template(
        "plants.html", plants=plants, search=search,
        room=room, size=size, light=light, water=water)


@app.route("/register", methods=("GET", "POST"))
def register():

    """
        Requires a unique username and password to create an account
        for user that is added to user database.

        Return: If successful, takes user to the profile page.

    """

    if request.method == "POST":
        # check to see if username exists already in mongo db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username already exists")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        # ensure passwords match
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

    """
        Requires the unique username and password used when registering
        to grant access to the users account.

        Return: If credentials correct takes user to profile page.

    """

    if request.method == "POST":
        # check if username already exists in mongo db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome Back {}".format(
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

    """
        Gets user data from database and displays all plants that current
        user created using the created_by key.

        Return: A list of plants created by current user from database.

    """

    # username from mongo db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        plants = list(mongo.db.plants.find({"created_by": username.lower()}))
        return render_template(
            "profile.html", username=username, plants=plants)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():

    """
        Deletes user cookies for current session.

        Return: Will take user back to the login page and require credentials
        to log back in.

    """

    # delete session cookies for user
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():

    """
        Adds data from form to database as a new data entry.

        Return: Add Plant form that adds inputs to the database.

    """

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
        return redirect(url_for("plants"))

    return render_template("add_plant.html")


@app.route("/edit<plant_id>", methods=["GET", "POST"])
def edit(plant_id):

    """
        Using the ID of the plant, pulls the current key value pairs from
        the database then updates these with any changes the user has made.

        Return: An edit form with the current data of the plant from the
        database with the option to change and submit changes.

    """

    if request.method == "POST":
        submit = {
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
        mongo.db.plants.update({"_id": ObjectId(plant_id)}, submit)
        flash("Plant Edited")

    plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})
    return render_template("edit.html", plant=plant)


@app.route("/delete<plant_id>")
def delete(plant_id):

    """
        Deletes the plant document in the database, finding it by its ID.

        Return: Deletes data and returns user to the plants page.

    """

    mongo.db.plants.remove({"_id": ObjectId(plant_id)})
    flash("Plant Deleted")
    return redirect(url_for("plants"))


@app.errorhandler(404)
def page_not_found(err):

    """
        Detects any errors in the url.

        Return: 404 page with a link back to browse.

    """

    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
