from application import db
from application.models import Base

class Wish(Base):
    # id
    #id = db.Column(db.Integer, primary_key=True)
    # date created
    #date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    # date modified, defaults to date created, but updates timestamp when modified
    #date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    #onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    approved = db.Column(db.Boolean, nullable=False)
    fulfilled = db.Column(db.Boolean, nullable=False)

    # whose wish
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.approved = False
        self.fulfilled = False
