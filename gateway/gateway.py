from flask import Flask, render_template, request,url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import InputRequired,Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/yaser/Downloads/PythonProjects/FlaskIntroduction/gateway/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db =SQLAlchemy(app)
app.app_context().push()
app.config['SECRET_KEY'] = 'thisisasecretkey'
bcrypt=Bcrypt(app)


login_manager=LoginManager()
login_manager.init_app(app)
login_manager.loginview ="login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/sample_page')
def sample_page():
    return render_template('components/sample-page.html')

@app.route('/cards')
def cards():
    return render_template('components/cards.html')



@app.route('/alerts')
def alerts():
    return render_template('components/alerts.html')



@app.route('/typography')
def typography():
    return render_template('components/typography.html')


@app.route('/forms')
def forms():
    return render_template('components/forms.html')



@app.route('/buttons')
def buttons():
    return render_template('components/buttons.html')

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')






@app.route('/tasks', methods=['GET','POST'])
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






@app.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username= form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
 
        
    return render_template('login.html',form=form)
 


@app.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')




@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




@app.route('/register', methods=['GET','POST'])
def register():
    form=RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username= form.username.data , password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))


    return render_template('register.html', form=form)




class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<Task %>' % self.id



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username=db.Column(db.String(20), nullable=False)
    password= db.Column(db.String(80), nullable=False)




class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(min=4,max=20)] , render_kw={"placeholder": "username"})
    password = PasswordField(validators=[InputRequired(),Length(min=4,max=20)], render_kw={"placeholder": "password"})
    submit = SubmitField("register")

    def validate_username(self,username):
        existing_user_username= User.query.filter_by(username=username.data).first()
        if existing_user_username: 
            raise ValidationError('The username already exist, please choose another one')



class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(),Length(min=4,max=20)],render_kw={"placeholder":"Username"} )
    password = PasswordField(validators=[InputRequired(),Length(min=4,max=5)],render_kw={"placeholder":"Password"})
    submit = SubmitField("login")




@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/tasks')
    except:
        return 'There was an error deleting that task'





#this is a test commit
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method=='POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/tasks')
        except:
            return 'There was an issue updating the task'
    else:
        return render_template('update.html', task=task)
    return ''



if __name__ == "__main__":
    app.run(debug=True)
