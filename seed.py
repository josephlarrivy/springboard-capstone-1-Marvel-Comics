from app import app, db
from models import db, User, List

db.drop_all()
db.create_all()

#####################

user1 = User(
    username = 'user1',
    password = 'user1',
    first_name = 'user1_first_name',
    last_name = 'user1_last_name',
    email = 'user1_email@test.com',
    lists = 'XN61QBX4N3I2INVJHWKB'
)

user2 = User(
    username='user2',
    password='user2',
    first_name='user2_first_name',
    last_name='user2_last_name',
    email='user2_email@test.com'
)

user3 = User(
    username='ExampleUser',
    password='ExampleUser',
    first_name='ExampleFirstName',
    last_name='ExampleLastName',
    email='example@example.com'
)


db.session.add_all([user1, user2, user3])
db.session.commit()

list1 = List(
    list_name = 'test_list_1',
    list_id = 'VP0M7SUK9ILL5KV499VV',
    username = 'user1'
)

db.session.add(list1)
db.session.commit()
