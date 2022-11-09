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

    issues = db.relationship('Issue', secondary='lists_issues', backref='lists')
    characters = db.relationship('Character', secondary='lists_characters', backref='lists')

    @classmethod
    def create_new_list(cls, list_name, list_id, username):
        return cls(list_name=list_name, list_id=list_id, username=username)


class ListIssue(db.Model):
    __tablename__ = 'lists_issues'

    list_id = db.Column(db.Text, db.ForeignKey('lists.list_id'), primary_key=True)
    issue_id = db.Column(db.Integer, db.ForeignKey('issues.issue_id'), primary_key=True)

    @classmethod
    def add_issue_to_list(cls, list_id, issue_id):
        return cls(list_id=list_id, issue_id=issue_id)


class Issue(db.Model):
    __tablename__ = 'issues'

    issue_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    thumbnail = db.Column(db.Text)
    description = db.Column(db.Text)
    # series = db.Column(db.Text)
    # series_id = db.Column(db.String)

    characters = db.relationship('Character', secondary='characters_issues', backref='issues')

    @classmethod
    def commit_issue_to_db(cls, issue_id, title, thumbnail, description):
        return cls(issue_id=issue_id, title=title, thumbnail=thumbnail, description=description)


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

    character_key = db.Column(db.Text, unique=True)
    character_id = db.Column(db.Integer)
    character_name = db.Column(db.Text, primary_key=True, unique=True)
    biography = db.Column(db.Text)
    thumbnail = db.Column(db.Text)

    @classmethod
    def commit_character_to_db(cls, character_key, character_id, character_name, biography, thumbnail):
        return cls(character_key=character_key, character_id=character_id, character_name=character_name, biography=biography, thumbnail=thumbnail)


class CharacterIssue(db.Model):
    __tablename__ = 'characters_issues'

    relationship_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    character_key = db.Column(db.Text, db.ForeignKey(
        'characters.character_key'))
    issue_id = db.Column(db.Integer, db.ForeignKey(
        'issues.issue_id'))

    @classmethod
    def link_character_to_issue(cls, character_key, issue_id):
        return cls(character_key=character_key, issue_id=issue_id)

#################################

