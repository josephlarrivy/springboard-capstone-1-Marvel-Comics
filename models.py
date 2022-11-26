from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
import os

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
    thumbnail = db.Column(db.Text)

    lists = db.relationship('List')
    comments = db.relationship('IssueComment')

    @classmethod
    def register_new_user(cls, username, password, first_name, last_name, email, thumbnail):
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode('utf8')
        return cls(username=username, password=hashed_utf8, first_name=first_name, last_name=last_name, email=email, thumbnail=thumbnail)
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
    series = db.Column(db.Text)
    series_id = db.Column(db.String)

    comments = db.relationship('IssueComment', backref='issue')

    characters = db.relationship('Character', secondary='characters_issues', backref='issues')

    @classmethod
    def commit_issue_to_db(cls, issue_id, title, thumbnail, description, series, series_id):
        return cls(issue_id=issue_id, title=title, thumbnail=thumbnail, description=description, series=series, series_id=series_id)


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
    biography = db.Column(db.Text, default='Not available')
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


class IssueComment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.String, primary_key=True)
    comment_content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    
    username = db.Column(db.String, db.ForeignKey('users.username'))

    issue_id = db.Column(db.Integer, db.ForeignKey('issues.issue_id'), nullable=False)

    @classmethod
    def link_comment_to_content(cls, comment_id, comment_content, timestamp, issue_id, username):
        return cls(comment_id=comment_id, comment_content=comment_content, timestamp=timestamp, issue_id=issue_id, username=username)




class SearchResults(db.Model):
    __tablename__ = 'search_results'
    
    search_term = db.Column(db.String, primary_key=True)
    search_results = db.Column(db.Text)
    series_search_results = db.Column(db.Text)

    @classmethod
    def search_results(cls, search_term):
        title_search_term = search_term.title()

        search_term = title_search_term.strip()

        directory = 'character_misspellings/misspelling_files'
        search_results = []

        for filename in os.listdir(directory):
            f = open(f'{directory}/{filename}', 'r')
            content = f.read()
            lines = content.splitlines()
            for line in lines:
                if search_term in line:
                    corrected_name = filename.removesuffix('.txt')
                    if corrected_name not in search_results:
                        search_results.append(corrected_name)
        search_results=search_results


        directory = 'series_names/series_names_files'
        series_search_results = {}

        for filename in os.listdir(directory):
            f = open(f'{directory}/{filename}', 'r')
            content = f.read()

            l = open(f'{directory}/{filename}', 'r')
            first_line = l.readline()
            series_name = first_line.removesuffix('\n')

            series_id = filename.removesuffix('.txt')

            split_terms = search_term.split()

            for term in split_terms:
                if term in content:
                    series_search_results[series_id] = series_name
            series_search_results = series_search_results

        return cls(search_term=search_term, search_results=search_results, series_search_results=series_search_results)
