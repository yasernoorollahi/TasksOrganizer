from flask import Blueprint, current_app, render_template
from common.db_setup_flask import db
from flask_login import  login_user, LoginManager, login_required, logout_user, current_user
from models.user_mdl import User

dashboard_bp = Blueprint('/dashboard', __name__)

def login_manager():
    login_manager = current_app.login_manager
    # login_manager.init_app(app)
    login_manager.loginview ="login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@dashboard_bp.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

