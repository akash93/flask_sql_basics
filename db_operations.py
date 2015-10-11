from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User,UserDetails,Base
from flask import Flask


engine = create_engine("sqlite:///users.db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

first_user = User(name='Akash Khan')
session.add(first_user)
session.commit()

first_detail = UserDetails(hostel_no='9',room_no=270,user=first_user)
session.add(first_detail)
session.commit()

