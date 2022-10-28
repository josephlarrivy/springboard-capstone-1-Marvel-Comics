from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

###############################

""" Models """

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True)
    username = db.Column(db.String(25), primary_key=True, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String)

    lists = db.relationship('Lists', backref='user')


class List(db.Model):
    
    __tablename__ = 'lists'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    list_name = db.Column(db.String(30),nullable=False)
    username = db.Column(db.Text, db.ForeignKey('users.username'), nullable=False)

    comics = db.relationship('Comic', secondary='lists_comics', backref='lists')


class ListComic(db.Model):

    __tablename__ = 'lists_comics'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))
    comic_id = db.Column(db.Integer, db.ForeignKey('comics.id'))


class Comic(db.Model):

    __tablename__ = 'comics'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
