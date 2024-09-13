from flask_login import UserMixin
from common.db_setup_flask import db
from models.role_mdl import Role



roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer() , db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer() , db.ForeignKey('role.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique= True)
    username = db.Column(db.String(20), nullable= False)
    password = db.Column(db.String(80), nullable = False)
    user_type = db.Column(db.Integer, nullable=False)
    roles = db.relationship('Role', secondary = roles_users , backref = db.backref('users', lazy= 'dynamic'))