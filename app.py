from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddUserForm, UserForm
from models import connect_db, db, User, List, ListTitle, ComicTitle
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///Springboard-Capstone-1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "W89#kU*67jL9##fhy@$hdj"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

toolbar = DebugToolbarExtension(app)

#################################

# MAIN ROUTES

@app.route('/')
def redirect_home():
    return redirect('/home')

@app.route('/home')
def show_homepage():
    user = User.query.get('user1')
    return render_template('/main/home.html', user=user)
