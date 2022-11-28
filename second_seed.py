from models import db, Issue, Character, CharacterIssue, IssueComment, User
from forms import DisposableUserForm
from app import app, db, show_characters, seed_characters, register_disposable
from keys import PUBLIC_KEY, PRIVATE_KEY
import random
import string
import time
import datetime
from datetime import datetime
from essential_generators import DocumentGenerator
from marvel import Marvel
marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)


# from flask import redirect
# import os
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///Marvel-Data"
app.config["SECRET_KEY"] = "W89#kU*67jL9##fhy@$hdj"


###########################################################

# os.environ['DATABASE_URL'] = "postgresql:///Marvel-Data"

db.create_all()
