from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2)]) #validators.Unique()])
    name = StringField("Display name", [validators.Length(min=2)])
    password = PasswordField("Password", [validators.Length(min=3)])#, EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("Confirm password")

    class Meta:
        csrf = False
