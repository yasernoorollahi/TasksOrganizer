from flask import Flask, render_template, request,url_for, redirect, current_app
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from common.db_setup_flask import DBSetup,db
from blueprints.auth.routes import auth_bp
from blueprints.dashboard.routes import dashboard_bp
from blueprints.tasks.routes import tasks_bp
from models.user_mdl import User



app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'

DBSetup.init_db(app)
bcrypt= Bcrypt(app)
login_manager=LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_request
def before_request():
    # Set bcrypt in the application context
    current_app.bcrypt = bcrypt
    current_app.login_manager= login_manager
 

app.register_blueprint(auth_bp, url_prefix = '/auth',template_folder='templates')
app.register_blueprint(dashboard_bp, url_prefix = '/dashboard', template_folder='templates')
app.register_blueprint(tasks_bp, url_prefix='/tasks', template_folder = 'templates')



@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')



#base.html =>
#line 103 => href="{{url_for('buttons')}}"
#line 112 =>   href="{{url_for('alerts')}}"
#line 122 => href="{{url_for('cards')}}"
#line 131 = >href="{{url_for('forms')}}"
#line 141 = >href="{{url_for('typography')}}"
#line 158 =>href="{{url_for('sample_page')}}"




if __name__ == '__main__':
    app.run()
    
# login_manager=LoginManager()
# login_manager.init_app(app)
# login_manager.loginview ="login"






# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))



# @app.route('/sample_page')
# def sample_page():
#     return render_template('components/sample-page.html')

# @app.route('/cards')
# def cards():
#     return render_template('components/cards.html')



# @app.route('/alerts')
# def alerts():
#     return render_template('components/alerts.html')



# @app.route('/typography')
# def typography():
#     return render_template('components/typography.html')


# @app.route('/forms')
# def forms():
#     return render_template('components/forms.html')



# @app.route('/buttons')
# def buttons():
#     return render_template('components/buttons.html')







# @app.route('/tasks', methods=['GET','POST'])
# @login_required
# def tasks():
#     if request.method == 'POST':
#         task_content= request.form['content']
#         new_task= Todo(content=task_content)
#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect('/tasks')
#         except:
#             return 'there was an error adding new task'
#     else:   
#         page = request.args.get('page',1 , type=int)
#         tasks = Todo.query.order_by(Todo.date_created.desc()).paginate(page = page, per_page=5)
#         return render_template('tasks.html', tasks=tasks)






# @app.route('/login', methods=['GET','POST'])
# def login():
#     form=LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username= form.username.data).first()
#         if user:
#             if bcrypt.check_password_hash(user.password, form.password.data):
#                 login_user(user)
#                 return redirect(url_for('dashboard'))
 
        
#     return render_template('login.html',form=form)
 


# @app.route('/dashboard', methods=['GET','POST'])
# @login_required
# def dashboard():
#     return render_template('dashboard.html')



# @app.route('/logout', methods=['GET','POST'])
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))




# @app.route('/register', methods=['GET','POST'])
# def register():
#     form=RegisterForm()

#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data)
#         new_user = User(username= form.username.data , password = hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for('login'))


#     return render_template('register.html', form=form)





# class RegisterForm(FlaskForm):
#     username = StringField(validators=[InputRequired(),Length(min=4,max=20)] , render_kw={"placeholder": "username"})
#     password = PasswordField(validators=[InputRequired(),Length(min=4,max=20)], render_kw={"placeholder": "password"})
#     submit = SubmitField("register")

#     def validate_username(self,username):
#         existing_user_username= User.query.filter_by(username=username.data).first()
#         if existing_user_username: 
#             raise ValidationError('The username already exist, please choose another one')



# # class LoginForm(FlaskForm):
# #     username = StringField(validators=[InputRequired(),Length(min=4,max=20)],render_kw={"placeholder":"Username"} )
# #     password = PasswordField(validators=[InputRequired(),Length(min=4,max=5)],render_kw={"placeholder":"Password"})
# #     submit = SubmitField("login")




# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)
#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/tasks')
#     except:
#         return 'There was an error deleting that task'





# #this is a test commit
# @app.route('/update/<int:id>', methods=['GET','POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)
#     if request.method=='POST':
#         task.content = request.form['content']
#         try:
#             db.session.commit()
#             return redirect('/tasks')
#         except:
#             return 'There was an issue updating the task'
#     else:
#         return render_template('update.html', task=task)
#     return ''


