from flask_login import UserMixin
from common.sqlite_setup import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username=db.Column(db.String(20), nullable=False)
    password= db.Column(db.String(80), nullable=False)