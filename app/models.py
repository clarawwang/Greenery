from datetime import datetime
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    info = db.relationship('UserInfo', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class UserInfo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.Column(db.String(100))
    week = db.Column(db.Integer)
    berry = db.Column(db.Integer)
    avocado = db.Column(db.Integer)
    tomato = db.Column(db.Integer)
    banana = db.Column(db.Integer)
    apple = db.Column(db.Integer)
    citrus = db.Column(db.Integer)
    beef = db.Column(db.Integer)
    lamb = db.Column(db.Integer)
    prawn = db.Column(db.Integer)
    fish = db.Column(db.Integer)
    pork = db.Column(db.Integer)
    chicken = db.Column(db.Integer)
    cheese = db.Column(db.Integer)
    egg = db.Column(db.Integer)
    tofu = db.Column(db.Integer)
    bean = db.Column(db.Integer)
    pea = db.Column(db.Integer)
    nut = db.Column(db.Integer)
    rice = db.Column(db.Integer)
    pasta = db.Column(db.Integer)
    oat = db.Column(db.Integer)
    bread = db.Column(db.Integer)
    potato = db.Column(db.Integer)
    milk = db.Column(db.Integer)
    pl_milk = db.Column(db.Integer)
    beer = db.Column(db.Integer)
    coffee = db.Column(db.Integer)
    wine = db.Column(db.Integer)
    tea = db.Column(db.Integer)
    ecar = db.Column(db.Integer)
    gcar = db.Column(db.Integer)
    train = db.Column(db.Integer)
    bus =  db.Column(db.Integer)
    plane =  db.Column(db.Integer)
    gas = db.Column(db.Integer)
    electricity = db.Column(db.Integer)
    fuel = db.Column(db.Integer)
    propane = db.Column(db.Integer)
    foodOut = db.Column(db.Integer)
    enOut = db.Column(db.Integer)
    transOut = db.Column(db.Integer)
    totalOut = db.Column(db.Integer)

    def __repr__(self):
        return '<Usage Today {}>'.format(self.totalOut)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))