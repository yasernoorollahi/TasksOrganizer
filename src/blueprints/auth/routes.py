from  flask import Blueprint, render_template, redirect, url_for, request
from models.user_mdl import User
from blueprints.auth.auth_forms import LoginForm
from flask_login import login_user
 
 

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username= form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
 
        
    return render_template('login.html',form=form)