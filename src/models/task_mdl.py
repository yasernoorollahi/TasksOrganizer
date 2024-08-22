from common.db_setup_flask import db
from datetime import datetime


class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime , default= datetime.now)
    
    
    def __repr__(self):
        return f'<Task {self.id}>'