from flask import Blueprint, render_template, redirect , request
from flask_login import login_required
from common.db_setup_flask import db 
#should change todo to tasks
from models.todo_mdl import Todo

tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/tasks', methods=['GET','POST'])
@login_required
def tasks():
    if request.method == 'POST':
        task_content= request.form['content']
        new_task= Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/tasks')
        except:
            return 'there was an error adding new task'
    else:   
        page = request.args.get('page',1 , type=int)
        tasks = Todo.query.order_by(Todo.date_created.desc()).paginate(page = page, per_page=5)
        return render_template('tasks.html', tasks=tasks)
