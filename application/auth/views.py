from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        flash("bazinga")
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    print("ATTEMPT LOGIN ON USER: " + form.username.data)
    print("")

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/login.html", form = form,
                               error = "No such username or password")


    print("Käyttäjä " + user.name + " tunnistettiin")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/register.html", form = RegisterForm())

    form = RegisterForm(request.form)
    # validate unique, pwd is +3 char
    #form.username

    if not form.validate():
        return render_template("auth/register.html", form = form)

    new_user = User(form.name.data, form.username.data, form.password.data)
    db.session().add(new_user)
    db.session().commit()

    # if form.username == "admin": makeAdmin
    login_user(new_user)
    return redirect(url_for("auth_login"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
