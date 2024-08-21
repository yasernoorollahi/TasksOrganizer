from flask import Blueprint, current_app, render_template , jsonify
from common.db_setup_flask import db
from flask_login import  login_user, LoginManager, login_required, logout_user, current_user
from models.todo_mdl import Todo



dashboard_bp = Blueprint('dashboard', __name__)




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



@dashboard_bp.route('/chart-data')
def get_chart_data():
    data ={
        'Name' : 'Earnings This Month:',
        'data' :[100,150,200,250,300,350,390,400]
    }
    data1 = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        'values': [30, 40, 35, 50, 49, 60, 70]
    }

    completed_tasks = Todo.query.order_by(Todo.completed==1).all()
    
    return jsonify(data1)
    