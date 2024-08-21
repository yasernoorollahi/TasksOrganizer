from flask import Blueprint, current_app, render_template
from common.db_setup_flask import db
from flask_login import  login_user, LoginManager, login_required, logout_user, current_user
from models.user_mdl import User

dashboard_bp = Blueprint('dashboard', __name__)



# def login_manager():
#     login_manager.loginview ="login"


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


@dashboard_bp.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@dashboard_bp.route('/sample_page')
def sample_page():
    return render_template('components/sample-page.html')


@dashboard_bp.route('/cards')
def cards():
    return render_template('components/cards.html')



@dashboard_bp.route('/alerts')
def alerts():
    return render_template('components/alerts.html')



@dashboard_bp.route('/typography')
def typography():
    return render_template('components/typography.html')


@dashboard_bp.route('/forms')
def forms():
    return render_template('components/forms.html')



@dashboard_bp.route('/buttons')
def buttons():
    return render_template('components/buttons.html')
