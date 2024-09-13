from flask_security import RoleMixin
from common.db_setup_flask import db 



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(),primary_key= True)
    role = db.Column(db.String(80), unique = True)
    description = db.Column(db.String(255))
    
