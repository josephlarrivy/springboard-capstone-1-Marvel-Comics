from app import app
from models import db, User, List, ListComic, Comic

db.drop_all()
db.create_all()

#####################

user1 = User(
    username = 'user1',
    password = 'user1',
    first_name = 'user1_first_name',
    last_name = 'user1_last_name',
    email = 'user1_email@test.com'
)

user2 = User(
    username='user2',
    password='user2',
    first_name='user2_first_name',
    last_name='user2_last_name',
    email='user2_email@test.com'
)

db.session.add_all([user1, user2])
db.session.commit()

