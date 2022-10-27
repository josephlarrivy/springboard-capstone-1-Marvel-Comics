from app import app
from models import db, User

db.drop_all()
db.create_all()

#####################

u1 = User(
    username = 'user1',
    password = 'user1',
    first_name = 'user_first_name',
    last_name = 'user_last_name',
    email = 'user1_email@test.com'
)