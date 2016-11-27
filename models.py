from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/production.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'User'
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    rep = db.Column(db.Boolean)

    def __init__(self, name, email=None, rep=False):
        self.name = name
        self.email = email
        self.rep = rep

    def __repr__(self):
        return '(%d:%s:%s:%s)' % (self.id, self.name, self.email, self.rep)

class ChatSession(db.Model):
    __tablename__ = 'ChatSession'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    participant1 = db.Column(db.Integer, db.ForeignKey('User.id'))
    participant2 = db.Column(db.Integer, db.ForeignKey('User.id'))

    def __init__(self, participant1, participant2):
        self.participant1 = participant1
        self.participant2 = participant2

    def __repr__(self):
        return '(%d:%s:%s:%s)' % (self.id, self.start_time, self.participant1, self.participant2)

class Message(db.Model):
    __tablename__ = 'Message'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('User.id'))
    chatSession = db.Column(db.Integer, db.ForeignKey('ChatSession.id'))
    message = db.Column(db.String(255))

    def __init__(self, user, chatSession, message):
        self.user = user
        self.chatSession = chatSession
        self.message = message

    def __repr__(self):
        return '(%d:%s:%s:[%s])' % (self.id, self.chatSession, self.user, self.message)


