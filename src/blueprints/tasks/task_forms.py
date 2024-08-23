from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired
from models.task_mdl import Tasks

class TaskForm(FlaskForm):
    title = StringField()
    description = StringField()
    