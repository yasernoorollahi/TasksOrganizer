from flask import Blueprint, current_app, render_template , jsonify
from common.db_setup_flask import db
from flask_login import  login_user, LoginManager, login_required, logout_user, current_user
from models.task_mdl import Tasks
from sqlalchemy import func


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
    
    daily_tasks = Tasks.query.with_entities(func.date(Tasks.created_date).label('date'), func.count(Tasks.id).label('count')).group_by(func.date(Tasks.created_date)).all()
    
    labels = [str(task.date) for task in daily_tasks]  # Dates as strings
    values = [task.count for task in daily_tasks]  # Corresponding counts

    # 3. Create the JSON structure
    tasks_data = {
    'labels': labels,  # List of dates
    'values': values   # List of counts for each date
}

    return jsonify(tasks_data)
    