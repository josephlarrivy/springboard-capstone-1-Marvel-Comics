from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddUserForm, DisposableUserForm, UserForm
from models import connect_db, db, User, List
from sqlalchemy.exc import IntegrityError
import string
import random
import requests
from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///Springboard-Capstone-1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SECRET_KEY"] = "W89#kU*67jL9##fhy@$hdj"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

toolbar = DebugToolbarExtension(app)
marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)

#################################

# Home/register/login/logout

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
        
        return redirect(f'/members/members_home/{username}')
    
    return render_template('/users/register.html', form=form)


@app.route('/register_disposable', methods=['GET', 'POST'])
def register_disposable():

    form = DisposableUserForm()

    if form.validate_on_submit():
        N=20
        username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        first_name = 'Guest'
        last_name = 'User'
        email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

        new_user = User.register_new_user(username, password, first_name, last_name, email)
        db.session.add(new_user)

        try:
            db.session.commit()
        except IntegrityError:
            flash('username already taken')
        
        session['username'] = username
        return redirect(f'/members/members_home/{username}')
    
    return render_template('/users/register_disposable.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def log_in_user():

    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            session['username'] = username
            return redirect(f'/members/members_home/{username}')
        else:
            flash('Invalid username/password combination')
            return render_template('/users/login.html', form=form)
    
    return render_template('/users/login.html', form=form)


@app.route('/logout')
def logout():
    if 'username' not in session:
        return redirect('/')
    else:
        session.pop('username')
        flash('logged out')
        return redirect('/')



################################

# routes for logged-in users

@app.route('/members/members_home/<username>')
def show_members_home(username):
    if 'username' not in session or username != session['username']:
        flash('must log in or register to view')
        return redirect('/login')
    curr_user = User.query.get(username)
    if curr_user.username == session['username']:
        return render_template('/members/members_home.html', user=curr_user, username=username)


@app.route('/members/<username>/profile')
def show_own_profile(username):
    user = User.query.get(username)
    if 'username' not in session:
        flash('must log in or register to view')
        return redirect('/login')
    elif username == session['username']:
        return render_template('/members/own_member_profile.html', user=user, username=username)
    else:
        return redirect(f'/members/{{user.username}}/view')


@app.route('/members/<view_user>/view')
def show_other_profile(view_user):
    if 'username' not in session:
        flash('must log in or register to view')
        return redirect('/login')
    else:
        view_user = User.query.get(view_user)
        username = session['username']
        return render_template('/members/other_member_profile.html', view_user=view_user, username=username)









@app.route('/test_view')
def test_comic_view():
    

    characters = marvel.characters

    # my_character = characters.all(name='Black Panther')['data']['results']
    my_character = characters.all(name='black widow')['data']['results']


    my_char = characters.all(nameStartsWith='Black')['data']['results']


    return render_template('/main/test_comic_view.html', my_character=my_character, my_char=my_char)
