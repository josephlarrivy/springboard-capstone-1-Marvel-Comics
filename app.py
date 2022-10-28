from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddUserForm, UserForm
from models import connect_db, db, User, List, ListComic, Comic
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
    return render_template('/main/home.html')

@app.route('/register', methods=['GET', 'POST'])
def register_new_user():

    form = AddUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data

        new_user = User.register_new_user(username, password, first_name, last_name, email)
        db.session.add(new_user)

        try:
            db.session.commit()
        except IntegrityError:
            flash('username already taken')
            return render_template('/users/register.html', form=form)

        return redirect('/home')
    
    return render_template('/users/register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def log_in_user():

    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username,password)
        if user:
            session['username'] = user.username
            return redirect('/')
        else:
            flash('Invalid username/password combination')
            return render_template('/users/login.html', form=form)
    
    return render_template('/users/login.html', form=form)
