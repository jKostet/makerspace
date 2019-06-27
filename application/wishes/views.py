from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.wishes.models import Wish
from application.wishes.forms import WishForm
from application.auth.models import User

@app.route("/wishes/", methods=["GET"])
def wishes_index():
    return render_template("wishes/list.html",
                            wishes = Wish.query.all(),
                            authors = User.query.all())

@app.route("/wishes/new/")
@login_required
def wishes_form():
    return render_template("wishes/new.html", form = WishForm())

@app.route("/wishes/", methods=["POST"])
@login_required
def wishes_create():
    form = WishForm(request.form) # Wish(request.form.get("name"))

    if not form.validate():
        print("INVALID INPUT")
        return render_template("wishes/new.html", form = form)

    print("ADDING TO Wishes.db" + request.form.get("name"))
    w = Wish(form.name.data, form.details.data)

    w.account_id = current_user.id

    w.details = form.details.data

    w.approved = form.approved.data
    w.fulfilled = form.fulfilled.data

    db.session().add(w)
    db.session().commit()

    return redirect(url_for("wishes_index"))

@app.route("/wishes/<wish_id>/u", methods=["POST"])
@login_required

def wishes_upvote(wish_id):
    w = Wish.query.get(wish_id)

    print("\n\n" + str(w.upvotes) + "\n\n")

    if (w.upvotes == None):
        w.upvotes = 1;
    else:
        w.upvotes += 1

    db.session().commit()
    wishAuthor = User.query.get(w.account_id)
    return render_template("wishes/wish.html", wish = w, user = current_user, wishAuthor = wishAuthor)

@app.route("/wishes/<wish_id>/", methods=["POST"])
@login_required
def wishes_set_approved(wish_id):
    w = Wish.query.get(wish_id)

    """
    getName = ("SELECT Wish.name FROM Wish WHERE Wish.id = " + wish_id + ";")
    data = str(db.engine.execute(getName))
    res = []
    for row in data:
        res.append({"a: ":row[0]})

    for row in res:
        print(row)

    apu = "pls help"
    print("\nSET APPROVED " + apu + "\n\n")
    """
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

@app.route("/wishes/<wish_id>/", methods=["GET"])
def single_wish_page(wish_id):
    w = Wish.query.get(wish_id)
    wishAuthor = User.query.get(w.account_id)
    return render_template("wishes/wish.html", wish = w, user = current_user, wishAuthor = wishAuthor)


@app.route("/wishes/<wish_id>/edit/", methods=["GET"])
def wishes_edit(wish_id):
    return render_template("wishes/edit.html", wish = Wish.query.get(wish_id), form = WishForm())

@app.route("/wishes/<wish_id>/edit/", methods=["POST"])
@login_required
def wish_ad_modify(wish_id):
    wish = wish.query.get(wish_id)
    form = wishForm(request.form)
    if not form.validate():
        return render_template("wishes/edit_ad.html", wish = wish.query.get(wish_id), form = form)

    wish.name = form.name.data
    wish.price = form.price.data

    db.session().commit()

    return redirect(url_for("wishes_index"))

@app.route("/wishes/<wish_id>/edit/delete/", methods=["POST"])
@login_required
def wishes_delete(wish_id):
    w = Wish.query.get(wish_id)

    db.session().delete(w)
    db.session().commit()

    return redirect(url_for("wishes_index"))
