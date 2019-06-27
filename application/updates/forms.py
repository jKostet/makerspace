from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class UpdateForm(FlaskForm):
    name = StringField("Update title", [validators.Length(min=2)])
    # Something else for big text box/field?
    message = StringField("Description", [validators.Length(min=2)])

    class Meta:
        csrf = False
