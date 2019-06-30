from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"

    #id = db.Column(db.Integer, primary_key=True)
    #date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    #date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    #                          onupdate=db.func.current_timestamp())

    # name is a display name instead of the (login) username.
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=True, default=False)

    # wishes by the username
    wishes = db.relationship("Wish", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_wishes_by_user(uid):
        stmt = text("SELECT Wish.id FROM Wish WHERE Wish.account_id = " + uid)
        res = db.execute(smtm)
