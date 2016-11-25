from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/production.db'
db = SQLAlchemy(app)


class User(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    rep  = db.Column(db.Boolean)
    sessions = db.relationship('Session', backref='user')

    def __init__(self, name, email, rep):
        self.name = name
        self.email = email
        self.rep = rep

    def __repr__(self):
        return '(%d:%s:%s:%s)' % (self.id, self.name, self.email, self.rep)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime(timezone=False))
    participant1 = db.Column(db.Integer, db.ForeignKey('user.id'))
    participant2 = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, start_time, participant1, participant2):
        self.start_time = start_time
        self.participant1 = participant1
        self.participant2 = participant2

    def __repr__(self):
        return '(%d:%s:%s:%s)' % (self.id, self.start_time, self.participant1, self.participant2)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    session = db.Column(db.Integer, db.ForeignKey('session.id'))
    message = db.Column(db.String(255))

    def __init__(self, user, session, message):
        self.user = user
        self.session = session
        self.message = message

    def __repr__(self):
        return '(%d:%s:%s:[%s])' % (self.id, self.user, self.user, self.message)


