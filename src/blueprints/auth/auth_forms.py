from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import InputRequired, Length, ValidationError
from models.user_mdl import User

class LoginForm(FlaskForm):
    username= StringField(validators=[InputRequired(),Length(min=4,max=20)],render_kw={'placeholder':'Username'} )
    password = PasswordField(validators=[InputRequired(),Length(min=4,max=5)],render_kw={'placeholder' : 'Password'})
    submit = SubmitField('login')
    


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(min=4,max=20)] , render_kw={'placeholder': 'username'})
    password = PasswordField(validators=[InputRequired(),Length(min=4,max=20)], render_kw={'placeholder': 'password'})
    submit = SubmitField("register")

    def validate_username(self,username):
        existing_user_username= User.query.filter_by(username=username.data).first()
        if existing_user_username: 
            raise ValidationError('The username already exist, please choose another one')