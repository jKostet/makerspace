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

@app.route("/wishes/a/<wish_id>/", methods=["POST"])
@login_required
def wishes_set_approved(wish_id):

    print("\nDEBUG PRINT: SET APPROVED\n")

    w = Wish.query.get(wish_id)
    w.approved = True
    db.session().commit()

    return redirect(url_for("wishes_index"))

@app.route("/wishes/ua/<wish_id>/", methods=["POST"])
@login_required
def wishes_undo_approved(wish_id):

    print("\nDEBUG PRINT: UNDO APPROVED\n")

    w = Wish.query.get(wish_id)
    w.approved = False
    db.session().commit()

    print("ree")

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


@app.route("/wishes/edit/<wish_id>/", methods=["GET"]) #,"POST"])
@login_required
def wishes_edit(wish_id):
#    if flask.request.method == 'POST':

    w = Wish.query.get(wish_id)
    f = WishForm()

    f.name.data = w.name
    f.details.data = w.details

    return render_template("wishes/edit.html", wish = w, form = f)


@app.route("/wishes/edit/<wish_id>/", methods=["POST"])
@login_required
def wishes_edit_save(wish_id):
    w = Wish.query.get(wish_id)
    f = WishForm(request.form)
    if not f.validate():
        return render_template("wishes/edit.html", wish = w, form = f)

    w.name = f.name.data
    w.details = f.details.data

    db.session().commit()

    return redirect(url_for("wishes_index"))

@app.route("/wishes/delete/<wish_id>/", methods=["POST"])
@login_required
def wishes_delete(wish_id):
    w = Wish.query.get(wish_id)

    db.session().delete(w)
    db.session().commit()

    return redirect(url_for("wishes_index"))
