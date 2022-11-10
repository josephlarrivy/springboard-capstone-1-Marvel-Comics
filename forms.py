from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import InputRequired, DataRequired, Length, Email

#############################


class AddUserForm(FlaskForm):
    """user registration"""
    username = StringField('Username', validators=[InputRequired(), Length(min=10)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)])
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired(), Email()])
    # thumbnail = StringField('thumbnail')

class DisposableUserForm(FlaskForm):
    """genreates randomized data for all fields required for registration"""
    username = StringField('Username')
    password = PasswordField('Password')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('email')
    thumbnail = HiddenField('thumbnail')

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

class CommentForm(FlaskForm):
    """Form for commenting"""
    comment_content = TextAreaField('Comment on this issue', validators=[InputRequired()])


class UserEditForm(FlaskForm):
    """Form for editing users."""
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[Length(min=6)])





######################

class IssueSearch(FlaskForm):
    issue_search_term = StringField('Search Issues', validators=[InputRequired()])
