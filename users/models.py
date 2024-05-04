from datetime import datetime
from init_db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    age = db.Column(db.Integer)
    regist_date = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(512), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    is_authenticated = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=False)
    is_anonymous = db.Column(db.Boolean, default=True)

    def get_id(self):
        return str(self.id)
    