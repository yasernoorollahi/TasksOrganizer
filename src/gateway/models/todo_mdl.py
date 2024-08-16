from common.db_setup_flask import db
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    content = db.Column(db.String(200), nullable =False)
    completed = db.Column(db.Integer , default=0)
    date_created = db.Column(db.DateTime,default= datetime.now)
    
    def __repr__(self):
        return f'<Task {self.id}>'