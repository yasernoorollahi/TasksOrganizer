from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True,unique=True)
   username = Column(String[30],nullable=False)
   password = Column(String[30], nullable=False)

 