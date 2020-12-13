from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager


class Data(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    first_name = db.Column(db.String(100))
    middle_initial = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    age = db.Column(db.INTEGER)
    home_town = db.Column(db.String(100))
    height = db.Column(db.INTEGER)
    weight = db.Column(db.INTEGER)
    scout_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, first_name, middle_initial, last_name, date_of_birth, age, home_town, height, weight):
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.home_town = home_town
        self.height = height
        self.weight = weight


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    scout = db.Column(db.Boolean, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
