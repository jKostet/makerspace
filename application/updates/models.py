from application import db
from application.models import Base

class Update(Base):
    # TODO: add name to Base?
    # Does it make sense, if name is
    # a display name for Users
    # and a title for Updates and Wishes?
    name = db.Column(db.String(144), nullable = False)
    # is db.String(n) n max length for database cell?
    # --> Apparently sqlite doesn't care, but postgresql on heroku does!
    # TODO: How should one store long texts in database?
    message = db.Column(db.String(144), nullable = False)

    # TODO: Implement Owner class for all that track object owner account_id?
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
