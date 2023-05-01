from app import db, bcrypt
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password_hash = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

    def __init__(self, email, password, first_name):
        self.email = email
        self.set_password(password)
        self.first_name = first_name

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
