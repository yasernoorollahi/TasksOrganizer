from flask_sqlalchemy import SQLAlchemy
from termcolor import colored,cprint

db =SQLAlchemy()

def init_db(app):
    print(colored('--- Database Initializing....','green', attrs=['bold']))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/yaser/Downloads/PythonProjects/FlaskIntroduction/src/test.db'
    print(colored('--- Database Path = Users/yaser/Downloads/PythonProjects/FlaskIntroduction/src/test.db',color='green',attrs=['bold']))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all() 
         