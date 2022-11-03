from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddUserForm, CharacterSearch, DisposableUserForm, UserForm, IssueSearch, CreateListForm
from models import connect_db, db, User, List, ListIssue, Issue, ListCharacter, Character
from sqlalchemy.exc import IntegrityError
import string
import random
import requests
from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///Springboard-Capstone-1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "W89#kU*67jL9##fhy@$hdj"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

toolbar = DebugToolbarExtension(app)
marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)

#################################

# home routes

@app.route('/')
def redirect_home():
    return redirect('/home')

@app.route('/home')
def show_homepage():
    if 'username' not in session:
        return render_template('/main/home.html')
    else:
        username = session['username']
        curr_user = User.query.get(username)
        return render_template('/members/members_home.html', user=curr_user, username=username)


##########################

# register/login/logout routes

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
        
        list_name = 'Wish List'
        list_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
        username = username

        new_list = List.create_new_list(list_name, list_id, username)

        db.session.add(new_list)
        db.session.commit()
       
        session['username'] = username
        return redirect(f'/members/members_home/{username}')
    
    return render_template('/users/register.html', form=form)


@app.route('/register_disposable', methods=['GET', 'POST'])
def register_disposable():

    form = DisposableUserForm()

    if form.validate_on_submit():
        username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
        first_name = 'Guest'
        last_name = 'User'
        email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

        new_user = User.register_new_user(username, password, first_name, last_name, email)
        db.session.add(new_user)

        try:
            db.session.commit()
        except IntegrityError:
            flash('username already taken')
        
        list_name = 'Wish List'
        list_id = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=20))
        username = username

        new_list = List.create_new_list(list_name, list_id, username)

        db.session.add(new_list)
        db.session.commit()
        
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

# member routes

@app.route('/members/members_home/<username>')
def show_members_home(username):
    if 'username' not in session:
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
        lists = user.lists
        return render_template('/members/own_member_profile.html', user=user, username=username, lists=lists)
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


#######################

# lists

@app.route('/members/create_list_form', methods=['GET', 'POST'])
def create_list_form():
    if 'username' not in session:
        flash('must log in or register to view')
        return redirect('/login')

    username = session['username']
    form = CreateListForm()

    if form.validate_on_submit():
        list_name = form.list_name.data
        list_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
        username = username

        new_list = List.create_new_list(list_name, list_id, username)

        db.session.add(new_list)
        db.session.commit()

        return redirect(f'/members/{username}/profile')

    else:
        return render_template('/members/create_list_form.html', form=form, username=username)


@app.route('/members/<username>/lists', methods=['GET', 'POST'])
def show_member_lists(username):
    if 'username' not in session:
        flash('must log in or register to view')
        return redirect('/login')
    username = session['username']

    curr_user = User.query.get(username)
    lists = curr_user.lists

    return render_template('/members/member_lists.html', username=username, lists=lists)


##########################

# search characters

@app.route('/search/characters', methods=['GET', 'POST'])
def search_characters():
    username = session['username']
    form = CharacterSearch()

    if form.validate_on_submit():
        character_search_term = form.character_search_term.data
        return redirect(f'/view_character/{character_search_term}')

    return render_template('/content/characters/search_characters.html', form=form, username=username)


# @app.route('/view_character/<character_name>')
# def show_characters(character_name):
#     username = session['username']
#     characters = marvel.characters
#     comics = marvel.comics

#     try:
#         single_character = characters.all(name=f'{character_name}')['data']['results'][0]

#         character_id = single_character['id']

#         character_data = characters.get(f'{character_id}')['data']['results'][0]

#         comic_series = characters.comics(f'{character_id}')['data']['results']

#         return render_template('/content/characters/view_character.html', username=username, single_character=single_character, character_id=character_id, comics=comics, character_data=character_data, comic_series=comic_series)
    
#     except IndexError:
#         flash('Character not found. Please check your spelling.')
#         return redirect('/search/characters')

##########################

# view issues

@app.route('/view_single_issue/<int:issue_id>', methods=['POST', 'GET'])
def view_single_issue(issue_id):
    username = session['username']
    comics = marvel.comics

    issue_data = comics.get(f'{issue_id}')['data']['results'][0]
    creators = comics.get(f'{issue_id}')['data']['results'][0]['creators']['items']
    characters = comics.get(f'{issue_id}')['data']['results'][0]['characters']['items']

    user = User.query.get(username)
    lists = user.lists

    return render_template('/content/issues/view_single_issue.html', issue_data=issue_data, creators=creators, characters=characters, user=user, lists=lists, username=username)

#########################

# add items to lists

@app.route('/add_issue/<int:issue_id>/to/<list_id>', methods=['GET', 'POST'])
def add_issue_to_list(issue_id, list_id):
    if 'username' not in session:
        flash('must log in or register to view')
        return redirect('/login')
    username = session['username']
    comics = marvel.comics
    
    issue_data = comics.get(f'{issue_id}')['data']['results'][0]

    issue_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
    thumbnail_path = issue_data['thumbnail']['path']
    thumbnail = f'{thumbnail_path}.jpg'
    title = issue_data['title']

    save_issue = Issue.commit_issue_to_db(issue_key, issue_id, thumbnail, title)
    db.session.add(save_issue)
    db.session.commit()

    commit_to_list = ListIssue.add_issue_to_list(list_id, issue_key)
    db.session.add(commit_to_list)
    db.session.commit()

    return redirect(f'/view_single_issue/{issue_id}')








@app.route('/view_character/<character_name>')
def show_characters(character_name):
    username = session['username']
    characters = marvel.characters
    comics = marvel.comics

    try:
        single_character = characters.all(name=f'{character_name}')[
            'data']['results'][0]

        character_id = single_character['id']

        character_data = characters.get(f'{character_id}')[
            'data']['results'][0]

        comic_series = characters.comics(f'{character_id}')['data']['results']

        user = User.query.get(username)
        lists = user.lists

        return render_template('/content/characters/view_character.html', username=username, single_character=single_character, character_id=character_id, comics=comics, character_data=character_data, comic_series=comic_series, lists=lists)

    except IndexError:
        flash('Character not found. Please check your spelling.')
        return redirect('/search/characters')


@app.route('/add_character/<character_name>/to/<list_id>', methods=['GET', 'POST'])
def add_character_to_list(character_name, list_id):
    if 'username' not in session:
        flash('must log in or register to view')
        return redirect('/login')
    username = session['username']
    comics = marvel.comics
    characters = marvel.characters

    single_character = characters.all(name=f'{character_name}')['data']['results'][0]

    character_key = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=20))
    character_name = single_character['name']
    thumbnail_path = single_character['thumbnail']['path']
    thumbnail = f'{thumbnail_path}.jpg'

    save_character = Character.commit_character_to_db(
        character_key, character_name, thumbnail)
    db.session.add(save_character)
    db.session.commit()

    commit_to_list = ListCharacter.add_character_to_list(list_id, character_key)
    db.session.add(commit_to_list)
    db.session.commit()

    return redirect(f'/view_character/{character_name}')































@app.route('/view_list_contents/<username>/<list_id>', methods=['GET', 'POST'])
def show_list_items(username, list_id):
    if 'username' not in session:
        flash('must log in or register to view')
        return redirect('/login')
    username = session['username']
    comics = marvel.comics

    list = List.query.get(list_id)
    issues = list.issues
    characters = list.characters

    

    return render_template('/members/view_list_contents.html', list=list, issues=issues, characters=characters, username=username)




    

















#####################
# use these to return a search that matches some keywords?

@app.route('/search/issues', methods=['GET', 'POST'])
def search_issues():
    username = session['username']
    form = IssueSearch()

    if form.validate_on_submit():
        issue_search_term = form.issue_search_term.data
        return redirect(f'/view_issues/{issue_search_term}')

    return render_template('/content/issues/search_issues.html', form=form, username=username)


@app.route('/view_issues/<issue_search_term>')
def show_searched_issues(issue_search_term):
    username = session['username']

    return render_template('/content/issues/view_issues.html', username=username)



@app.route('/view/issues', methods=['GET', 'POST'])
def view_issues():
    username = session['username']
    comics = marvel.comics

    get_comics = comics.all()['data']['results']

    return render_template('/content/issues/view_issues.html', username=username, get_comics=get_comics, comics=comics)
