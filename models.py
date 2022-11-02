from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

###############################

""" Models """

class User(db.Model):

    __tablename__ = 'users'

    username = db.Column(db.String(25), primary_key=True, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String)

    lists = db.relationship('List')

    @classmethod
    def register_new_user(cls, username, password, first_name, last_name,email):
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode('utf8')
        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name)

    @classmethod
    def authenticate(cls, username, password):
        u = User.query.filter_by(username=username).first()
        if u and bcrypt.check_password_hash(u.password, password):
            return u
        else:
            return False


class List(db.Model):
    
    __tablename__ = 'lists'
    
    list_name = db.Column(db.String(25), nullable=False)
    list_id = db.Column(db.Text, unique=True, primary_key=True, nullable=False)
    username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

    @classmethod
    def create_new_list(cls, list_name, list_id, username):
        return cls(list_name=list_name, list_id=list_id, username=username)

    user = db.relationship('User')