from flask import render_template, request, redirect, url_for

from application import app, db
from application.wishes.models import Wish
from application.wishes.forms import WishForm

@app.route("/wishes/new/")
def wishes_form():
    return render_template("wishes/new.html", form = WishForm())

@app.route("/wishes/", methods=["POST"])
def wishes_create():
    form = WishForm(request.form) # Wish(request.form.get("name"))

    if not form.validate():
        print("INVALID INPUT")
        return render_template("wishes/new.html", form = form)

    print("ADDING TO Wishes.db" + request.form.get("name"))
    w = Wish(form.name.data)
    w.approved = form.approved.data
    w.fulfilled = form.fulfilled.data
    w.account_id = current_user.id

    db.session().add(w)
    db.session().commit()

    return redirect(url_for("wishes_index"))

@app.route("/wishes/<wish_id>/", methods=["POST"])
def wishes_set_approved(wish_id):
    w = Wish.query.get(wish_id)
    w.approved = True
    # TODO: Tsekkaa "done" -> wish/equipment request approved?
    db.session().commit()

    return redirect(url_for("wishes_index"))

# TODO: add button to mark wishes as fulfilled
"""def wishes_set_fulfilled(wish_id):
    w = Wish.query.get(wish_id)
    w.fulfilled = True
    # TODO: Tsekkaa "done" -> wish/equipment request approved?
    db.session().commit()

    return redirect(url_for("wishes_index"))
"""
