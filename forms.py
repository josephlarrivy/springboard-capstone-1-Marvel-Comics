from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired

#############################


class AddUserForm(FlaskForm):
    """user registration"""
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired()])

class DisposableUserForm(FlaskForm):
    """genreates randomized data for all fields required for registration"""
    username = StringField('Username')
    password = PasswordField('Password')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('email')

class UserForm(FlaskForm):
    """user login"""
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class CharacterSearch(FlaskForm):
    """search for a character"""
    character_search_term = StringField('Search Characters', validators=[InputRequired()])

class CreateListForm(FlaskForm):
    """name and create a list"""
    list_name = StringField('List Name', validators=[InputRequired()])


# class UserEditForm(FlaskForm):

######################

class IssueSearch(FlaskForm):
    issue_search_term = StringField('Search Issues', validators=[InputRequired()])



