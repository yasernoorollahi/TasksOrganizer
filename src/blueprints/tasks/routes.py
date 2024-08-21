from flask import Blueprint, render_template, redirect , request,url_for
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
        new_task= Todo(content=task_content,completed=1)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('tasks.tasks'))
        except:
            return 'there was an error adding new task'
    else:   
        page = request.args.get('page',1 , type=int)
        tasks = Todo.query.order_by(Todo.date_created.desc()).paginate(page = page, per_page=5)
        return render_template('tasks.html', tasks=tasks)



@tasks_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('tasks.tasks'))
    except:
        return 'There was an error deleting that task'


@tasks_bp.route('/update/<int:id>', methods=['GET','POST'])
@login_required
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method=='POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect(url_for('tasks.tasks'))
        except:
            return 'There was an issue updating the task'
    else:
        return render_template('update.html', task=task)
    return ''
