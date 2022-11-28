from keys import PUBLIC_KEY, PRIVATE_KEY
import random
import string
import time
import datetime
from datetime import datetime
from essential_generators import DocumentGenerator
from marvel import Marvel
marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)


from app import app, db, show_characters, seed_characters, register_disposable
from models import db, Issue, Character, CharacterIssue, IssueComment,User
from forms import DisposableUserForm


# from flask import redirect
# import os
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///Marvel-Data"
app.config["SECRET_KEY"] = "W89#kU*67jL9##fhy@$hdj"


###########################################################

# os.environ['DATABASE_URL'] = "postgresql:///Marvel-Data"

db.drop_all()
db.create_all()

def show_characters(character_name):
    
    characters = marvel.characters
    comics = marvel.comics

    single_character = characters.all(name=f'{character_name}')['data']['results'][0]

    character_id = single_character['id']

    # character_data = characters.get(f'{character_id}')['data']['results'][0]

    comic_series = characters.comics(f'{character_id}')['data']['results']

    character_key = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=20))
    character_id = single_character['id']
    character_name = single_character['name'].title()
    biography = single_character['description']
    thumbnail_path = single_character['thumbnail']['path']
    thumbnail = f'{thumbnail_path}.jpg'

    save_character = Character.commit_character_to_db(
        character_key, character_id, character_name, biography, thumbnail)
    db.session.add(save_character)
    db.session.commit()

    for comic in comic_series:
        series = marvel.series
        issue_id = comic['id']

        issue_data = comics.get(f'{issue_id}')['data']['results'][0]
        url = issue_data['series']['resourceURI']
        series_id = url.removeprefix(
            'http://gateway.marvel.com/v1/public/series/')
        series_data = series.get(series_id)['data']['results'][0]
        series = series_data['title']

        title = issue_data['title']
        thumbnail_path = issue_data['thumbnail']['path']
        thumbnail = f'{thumbnail_path}.jpg'
        description = issue_data['description']
        # character = single_character['name']

        if Issue.query.get(issue_id):
            pass
        else:
            commit_issue = Issue.commit_issue_to_db(issue_id, title, thumbnail, description, series, series_id)
            db.session.add(commit_issue)
            db.session.commit()

        connect_character_issue = CharacterIssue.link_character_to_issue(
            character_key, issue_id)
        db.session.add(connect_character_issue)
        db.session.commit()








print('checkpoint - seed start ###########')

for character in seed_characters:
    time.sleep(2)
    show_characters(character)
    print('checkpoint - timeout activated')

print('checkpoint - done seeding characters')



print('checkpoint - seed a user')

username = 'seed_user'
password = ''.join(random.choices(
    string.ascii_uppercase + string.digits, k=20))
first_name = 'Seed'
last_name = 'User'
email = ''.join(random.choices(
    string.ascii_uppercase + string.digits, k=12))
thumbnail = 'captain.png'

new_user = User.register_new_user(
    username, password, first_name, last_name, email, thumbnail)
db.session.add(new_user)

print('checkpoint - user seeded')

##############################

print('checkpoint - start seeding comments')

issues_for_seed_comments = []

first_seed_character = seed_characters[0]
featured_character1 = Character.query.get(first_seed_character.title())
issues1 = featured_character1.issues

for issue in issues1:
    issues_for_seed_comments.append(issue.issue_id)

for issue in issues_for_seed_comments:
    gen = DocumentGenerator()

    comment_content = (gen.sentence())
    comment_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
    timestamp = datetime.now()
    issue_id = issue
    username = 'seed_user'

    new_comment = IssueComment.link_comment_to_content(comment_id, comment_content, timestamp, issue_id, username)

    db.session.add(new_comment)
    db.session.commit()
    print('checkpoint - comment seeded')


print('checkpoint - seed complete ##############')

#############################################################

# user1 = User(
#     username = 'user1',
#     password = 'user1',
#     first_name = 'user1_first_name',
#     last_name = 'user1_last_name',
#     email = 'user1_email@test.com',
#     thumbnail = 'groot.png',
#     lists='VP0M7SUK9ILL5KV499VV'
# )
# db.session.add(user1)
# db.session.commit()
# print('checkpoint1')


# list1 = List(
#     list_name = 'test_list_1',
#     list_id='VP0M7SUK9ILL5KV499VV',
#     username = 'user1'
# )
# db.session.add(list1)
# db.session.commit()
# print('checkpoint2')



# listissue1 = ListIssue(
#     list_id='VP0M7SUK9ILL5KV499VV',
#     issue_id='asdf1234'
# )
# db.session.add(listissue1)
# db.session.commit()

# # need to update Issue to include all data from model
# issue1 = Issue(
#     issue_id = 1,
#     title = 'comic1',
#     thumbnail = 'test',
#     description = 'description1',
#     characters = 'character5',
#     series = 'series1',
#     series_id = 1
# )
# db.session.add(issue1)
# db.session.commit()

# listcharacter1 = ListCharacter(
#     list_id='VP0M7SUK9ILL5KV499VV',
#     character_key = 'qwertyuiop'
# )
# db.session.add(listcharacter1)
# db.session.commit()

# character1 = Character(
#     character_key='qwertyuiop',
#     character_id = '123456',
#     thumbnail = 'thumbnail1',
#     name = 'character5'
# )
# db.session.add(character1)
# db.session.commit()

# characterissue1 = CharacterIssue(
#     character_key='qwertyuiop',
#     issue_id='asdf1234'
# )

# # series1 = Series(
# #     series_id = 3498,
# #     series_name = 'test_series'
# # )

# # seriesissue1 = SeriesIssue(
# #     series_id = 3498,
# #     issue_id = 1
# # )










########################################


# def populate_a_user():
#     print('registering')
#     register_disposable()
#     print('registed')

# populate_a_user()

# session['username'] = username
# characters = ['Loki', 'Rocket Raccoon']


# def populate_starter_data():
#     for character in characters:
#         print(character)
#         show_characters(f'/view_character/{character}')


# populate_starter_data()
