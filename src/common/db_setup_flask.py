from flask_sqlalchemy import SQLAlchemy
from common.local_enums import Framework
from termcolor import colored
from flask_migrate import Migrate


db =SQLAlchemy()
db_initialized= False

class DBSetup:


    def init_db(app):
        global db_initialized
        if db_initialized:
            return
        print(colored('--- Database Initializing....','green', attrs=['bold']))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/yaser/Downloads/PythonProjects/FlaskIntroduction/src/test.db'
        print(colored('--- Database Path = Users/yaser/Downloads/PythonProjects/FlaskIntroduction/src/test.db',color='green',attrs=['bold']))
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)
        migrate = Migrate(app,db)
        print(colored('after init app',color='red', attrs=['bold']))
        with app.app_context():
            db.create_all()
            print(colored('inside with',color='red',attrs=['bold'])) 
        db_initialized =True
         