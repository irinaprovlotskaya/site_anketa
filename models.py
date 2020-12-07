from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Questions(db.Model):
    __tablename__="questions"

    question_id = db.Column('question_id', db.Integer, primary_key=True)
    questions = db.Column('questions', db.Text)


class Result(db.Model):
    __tablename__="answers"

    answers_id = db.Column('answers_id', db.Integer, primary_key=True)
    ask = db.Column('ask', db.Text)
    ask2 = db.Column('ask2', db.Text)
    ask3 = db.Column('ask3', db.Text)
    ask4 = db.Column('ask4', db.Text)
    ask5 = db.Column('ask5', db.Text)
    ask6 = db.Column('ask6', db.Text)


class User(db.Model):
    __tablename__="user"

    person_id = db.Column('person_id', db.Integer, primary_key=True)
    gender = db.Column('gender', db.Text)
    age = db.Column('age', db.Integer)