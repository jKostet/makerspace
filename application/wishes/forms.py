from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class WishForm(FlaskForm):
    name = StringField("Wish title")
    approved = BooleanField("Approved")
    fulfilled = BooleanField("Fulfilled")

    class Meta:
        csrf = False
