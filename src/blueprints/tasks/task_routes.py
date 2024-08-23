from flask import Blueprint, render_template, redirect , request,url_for
from flask_login import login_required
from common.db_setup_flask import db 
from blueprints.tasks.task_forms import TaskForm
#should change todo to tasks
from models.task_mdl import Tasks


tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/tasks', methods=['GET','POST'])
@login_required
def tasks():
    form = TaskForm()
    if form.validate_on_submit():
        # task_content= request.form['content']
        title = form.title.data
        description = form.description.data
        completed = form.completed.data
        created_date  = form.created_date.data
        due_date = form.due_date.data
        # assigned_to = form.assigned_to.data
        
        new_task= Tasks(title= title,description=description, completed=completed, created_date=created_date, due_date=due_date )
        # new_task= Tasks(title=task_content,completed=1)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('tasks.tasks'))
        except:
            return 'there was an error adding new task'
    else:   
        page = request.args.get('page',1 , type=int)
        tasks = Tasks.query.order_by(Tasks.created_date.desc()).paginate(page = page, per_page=5)
        return render_template('tasks.html', tasks=tasks, form=form)



@tasks_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    task_to_delete = Tasks.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('tasks.tasks'))
    except:
        return 'There was an error deleting that task'


@tasks_bp.route('/update/<int:id>', methods=['GET','POST'])
@login_required
def update(id):
    task = Tasks.query.get_or_404(id)
    if request.method=='POST':
        task.title = request.form['content']
        try:
            db.session.commit()
            return redirect(url_for('tasks.tasks'))
        except:
            return 'There was an issue updating the task'
    else:
        return render_template('update.html', task=task)
    return ''
