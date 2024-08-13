from enum import Enum

class Colors(Enum):
    RED= 'red'
    BLUE= 'blue'
    GREEN= 'green'


class UserRole(Enum):
    ADMIN='admin'
    USER='user'
    GUEST='guest'



class Framework(Enum):
    NONE = 'none'
    SQLALCHEMY = 'sqlalchemy'
    DJANGO = 'django'
    MONGODB = 'mongodb'
    REDIS = 'redis'
    ELASTICSEARCH = 'elasticsearch'
    POSTGRESQL = 'postgresql'
    MYSQL = 'mysql'
    SQLSERVER = 'sqlserver'
    ORACLE = 'oracle'
    