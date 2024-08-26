from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, DateField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,InputRequired
from models.task_mdl import Tasks
from models.user_mdl import User
from common.local_enums import TaskStatus, PriorityLevel

class TaskForm(FlaskForm):
    title = StringField(validators=[InputRequired()])
    description = TextAreaField(validators=[InputRequired()])
    completed= BooleanField()
    created_date =DateField()
    due_date = DateField()
    submit = SubmitField('Add New Task')
    