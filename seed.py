from app import app, db
from models import db, User, List, ListIssue, Issue, ListCharacter, Character, CharacterIssue

db.drop_all()
db.create_all()

#####################

user1 = User(
    username = 'user1',
    password = 'user1',
    first_name = 'user1_first_name',
    last_name = 'user1_last_name',
    email = 'user1_email@test.com',
    lists='VP0M7SUK9ILL5KV499VV'
)
db.session.add(user1)
db.session.commit()

list1 = List(
    list_name = 'test_list_1',
    list_id='VP0M7SUK9ILL5KV499VV',
    username = 'user1'
)
db.session.add(list1)
db.session.commit()

listissue1 = ListIssue(
    list_id='VP0M7SUK9ILL5KV499VV',
    issue_id='asdf1234'
)
db.session.add(listissue1)
db.session.commit()

# need to update Issue to include all data from model
issue1 = Issue(
    issue_id = 1,
    title = 'comic1',
    thumbnail = 'test',
    description = 'description1',
    characters = 'character5',
    series = 'series1',
    series_id = 1
)
db.session.add(issue1)
db.session.commit()

listcharacter1 = ListCharacter(
    list_id='VP0M7SUK9ILL5KV499VV',
    character_key = 'qwertyuiop'
)
db.session.add(listcharacter1)
db.session.commit()

character1 = Character(
    character_key='qwertyuiop',
    character_id = '123456',
    thumbnail = 'thumbnail1',
    name = 'character5'
)
db.session.add(character1)
db.session.commit()

characterissue1 = CharacterIssue(
    character_key='qwertyuiop',
    issue_id='asdf1234'
)

# series1 = Series(
#     series_id = 3498,
#     series_name = 'test_series'
# )

# seriesissue1 = SeriesIssue(
#     series_id = 3498,
#     issue_id = 1
# )