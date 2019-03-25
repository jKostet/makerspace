from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class WishForm(FlaskForm):
    name = StringField("Wish title", [validators.Length(min=2)])
    approved = BooleanField("Approved")
    fulfilled = BooleanField("Fulfilled")

    class Meta:
        csrf = False
