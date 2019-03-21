from application import app, db
from flask import render_template, request, redirect, url_for
from application.wishes.models import Wish

@app.route("/wishes/new/")
def wishes_form():
    return render_template("wishes/new.html")

@app.route("/wishes/", methods=["POST"])
def wishes_create():
    print(request.form.get("name"))
    apu = Wish(request.form.get("name"))

    db.session().add(apu)
    db.session().commit()

    return redirect(url_for("wishes_index"))

@app.route("/wishes/<wish_id>/", methods=["POST"])
def wishes_set_done(wish_id):
    w = Wish.query.get(wish_id)
    w.done = True
    # TODO: Tsekkaa "done" -> wish/equipment request approved?
    db.session().commit()

    return redirect(url_for("wishes_index"))

@app.route("/wishes/", methods=["GET"])
def wishes_index():
    return render_template("wishes/list.html", wishes = Wish.query.all())
