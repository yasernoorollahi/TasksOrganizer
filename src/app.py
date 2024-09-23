from flask import Flask, render_template, request,url_for, redirect, current_app
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from common.db_setup_flask import DBSetup,db
from blueprints.auth.auth_routes import auth_bp
from blueprints.dashboard.dashboard_routes import dashboard_bp
from blueprints.tasks.task_routes import tasks_bp
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



if __name__ == '__main__':
    app.run()
 