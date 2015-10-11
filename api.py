from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User,UserDetails,Base
from flask import jsonify

app = Flask(__name__)

engine = create_engine("sqlite:///users.db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/',methods=['GET'])
def get_users():
    user = session.query(UserDetails).all()
    return jsonify(hostel_no=user[0].hostel_no,room_no=user[0].room_no)

if __name__=='__main__':
    app.run()             
