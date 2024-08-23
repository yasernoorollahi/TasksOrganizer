from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, DateField, SubmitField 
from wtforms.validators import DataRequired
from models.task_mdl import Tasks
from models.user_mdl import User
from common.local_enums import TaskStatus, PriorityLevel

class TaskForm(FlaskForm):
    title = StringField()
    description = StringField()
    completed= BooleanField()
    created_date =DateField()
    due_date = DateField()
    status = TaskStatus()
    priority = PriorityLevel()
    assigned_to = User()
    submit = SubmitField()
    