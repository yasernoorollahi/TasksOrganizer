from  flask import Blueprint, render_template, redirect, url_for, request, current_app,g
from models.user_mdl import User
from blueprints.auth.auth_forms import LoginForm, RegisterForm
from flask_login import login_user
from common.db_setup_flask import db


 

auth_bp = Blueprint('auth', __name__)




@auth_bp.route('/login', methods=['GET','POST'])
def login():
    bcrypt = current_app.bcrypt
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username= form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard.dashboard'))
 
        
    return render_template('login.html',form=form)



@auth_bp.route('/register', methods=['GET','POST'])
def register():
    bcrypt = current_app.bcrypt
    form=RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username= form.username.data , password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))


    return render_template('register.html', form=form)