import sys
from sqlalchemy import Column,Integer,ForeignKey,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(255),nullable = False)

class UserDetails(Base):
    __tablename__ = "user_details"
    id =  Column(Integer,primary_key=True)
    hostel_no = Column(String(3),nullable=False)
    room_no = Column(Integer,nullable=False)
    user_id =  Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

engine = create_engine("sqlite:///users.db")
Base.metadata.create_all(engine)




