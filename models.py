from app import db
from flask_login import UserMixin
import datetime

class User(UserMixin, db.Model):
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), unique = True)
    phone = db.Column(db.String(60), unique = True)
    password = db.Column(db.String(30))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)