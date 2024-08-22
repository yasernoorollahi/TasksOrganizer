from common.db_setup_flask import db
from datetime import datetime
from sqlalchemy import Enum , ForeignKey
from common.local_enums import TaskStatus, PriorityLevel
class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime , default= datetime.now)
    due_date = db.Column(db.DateTime , nullable =True)
    status =db.Column(Enum(TaskStatus) , default = TaskStatus.TODO) 
    priority = db.Column(Enum(PriorityLevel) , default = PriorityLevel.LOW)
    assigned_to = db.Column(db.Integer, ForeignKey('user.id'), nullable =True )
    
    
    
    def __repr__(self):
        return f'<Task {self.id}>'