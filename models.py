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

    username = db.Column(db.Text, primary_key=True, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
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
    
    list_name = db.Column(db.Text, nullable=False)
    list_id = db.Column(db.Text, unique=True, primary_key=True, nullable=False)
    username = db.Column(db.Text, db.ForeignKey('users.username'), nullable=False)

    user = db.relationship('User')
    issues = db.relationship('Issue', secondary='lists_issues', backref='lists')
    characters = db.relationship('Character', secondary='lists_characters', backref='lists')

    @classmethod
    def create_new_list(cls, list_name, list_id, username):
        return cls(list_name=list_name, list_id=list_id, username=username)


class ListIssue(db.Model):

    __tablename__ = 'lists_issues'

    list_id = db.Column(db.Text, db.ForeignKey('lists.list_id'), primary_key=True)
    issue_key = db.Column(db.Text, db.ForeignKey('issues.issue_key'), primary_key=True)

    @classmethod
    def add_issue_to_list(cls, list_id, issue_key):
        return cls(list_id=list_id, issue_key=issue_key)


class Issue(db.Model):

    __tablename__ = 'issues'

    issue_key = db.Column(db.Text, primary_key=True, unique=True)
    issue_id = db.Column(db.Integer)
    thumbnail = db.Column(db.Text)
    title = db.Column(db.Text)

    @classmethod
    def commit_issue_to_db(cls, issue_key, issue_id, thumbnail, title):
        return cls(issue_key=issue_key, issue_id=issue_id, thumbnail=thumbnail, title=title)

##################


class ListCharacter(db.Model):

    __tablename__ = 'lists_characters'

    list_id = db.Column(db.Text, db.ForeignKey(
        'lists.list_id'), primary_key=True)
    character_key = db.Column(db.Text, db.ForeignKey(
        'characters.character_key'), primary_key=True)

    @classmethod
    def add_character_to_list(cls, list_id, character_key):
        return cls(list_id=list_id, character_key=character_key)


class Character(db.Model):

    __tablename__ = 'characters'

    character_key = db.Column(db.Text, primary_key=True, unique=True)
    character_name = db.Column(db.Text)
    thumbnail = db.Column(db.Text)

    @classmethod
    def commit_character_to_db(cls, character_key, character_name, thumbnail):
        return cls(character_key=character_key, character_name=character_name, thumbnail=thumbnail)
