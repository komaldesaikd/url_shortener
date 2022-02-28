from extensions import db
from datetime import datetime
from random import choices
import string


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(1024))
    short_url = db.Column(db.String(6))    
    




        









 