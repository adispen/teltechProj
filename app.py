from flask import Flask, render_template, session, request, jsonify, Response, abort
from flask.ext.socketio import SocketIO, emit, disconnect
from models import db, User, ChatSession, Message
import json

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

usernames = {}
number_of_users = 0
chatSessionID = None

def create_session():
    global chatSessionID
    users = []
    for user in usernames.keys():
        users.append(user)

    user1 = User.query.filter_by(email=users[0]).first()
    user2 = User.query.filter_by(email=users[1]).first()
    chat_session = ChatSession(user1.id, user2.id)
    db.session.add(chat_session)
    db.session.commit()
    chatSessionID = chat_session.id
    print chatSessionID

@app.route('/get_reps', methods=['GET'])
def get_reps():
        reps = User.query.filter_by(rep=True).all()
        repList = []
        for item in reps:
            print item.id
            print item.name
            repJson = {
                'userID' : item.id,
                'username' : item.name
            }
            repList.append(repJson)
            
        return Response(json.dumps(repList), mimetype='application/json') 

@app.route('/change_rep', methods=['PUT'])
def change_rep():
        repID = request.args.get('repID')
        new_name = request.args.get('new_name')
        if not repID or not new_name:
            return 'Bad request', 400


        print(repID)
        print(new_name)

@app.route('/')
def index():
	return render_template('content.html')

@app.route('/chat')
def chat():
	return render_template('chat.html')


# When the client emits 'connection', this listens and executes
@socketio.on('connect', namespace='/chat')
def user_connected():
	print('User connected')


# When the client emits 'new message', this listens and executes
@socketio.on('new message', namespace='/chat')
def new_message(data):
        global chatSessionID
        message = Message(session['userID'], chatSessionID, data)

	emit('new message',{ 
            'username' : session['username'],
	    'message': data 
        }, broadcast=True )

        db.session.add(message)
        db.session.commit()

# When client emits 'add rep' this listens and executes
@socketio.on('add rep', namespace='/chat')
def add_rep(data):
	print 'Adding Rep'
	global usernames
	global number_of_users

	session['username'] = data
        repname = 'rep_' + session['username']
	usernames[repname] = session['username']
        print usernames

        user = User.query.filter_by(email=repname, rep=True).first()
        if not user:
            user = User(session['username'], repname, True)
            db.session.add(user)
            db.session.commit()

        session['userID'] = user.id

	number_of_users += 1;
        if number_of_users == 2:
            create_session()

	emit('login', { 'numUsers' : number_of_users })
	emit('user joined', { 'username' : session['username'], 'numUsers': number_of_users }, broadcast=True)

# When client emits 'add user' this listens and executes
@socketio.on('add user', namespace='/chat')
def add_user(data):
	print 'Adding User'
	global usernames
	global number_of_users

	session['username'] = data['username']
        session['email'] = data['email']
	usernames[data['email']] = session['username']
        print usernames

        user = User.query.filter_by(email=session['email'], rep=False).first()
        if not user:
            user = User(session['username'], session['email'])
            db.session.add(user)
            db.session.commit()

        session['userID'] = user.id

	number_of_users += 1;
        if number_of_users == 2:
            create_session()

	emit('login', { 'numUsers' : number_of_users })
	emit('user joined', { 'username' : session['username'], 'numUsers': number_of_users }, broadcast=True)
        emit('user email', { 'email' : session['email'], 'username' : session['username'] }, broadcast=True)


@socketio.on('typing', namespace='/chat')
def typing_response():
	try:
		emit('typing', { 'username' : session['username'] }, broadcast=True )
	except:
		pass


@socketio.on('stop typing', namespace='/chat')
def stop_typing():
	try:
		emit('stop typing', { 'username' : session['username'] }, broadcast = True)
	except:
		pass


@socketio.on('disconnect', namespace='/chat')
def disconnect():
	global usernames
	global number_of_users
        global chatSessionID


	try:
		del usernames[session['email']]
		number_of_users -= 1
                chatSessionID = None
		emit('user left', { 'username' : session['username'], 'numUsers' : number_of_users}, broadcast=True)

	except:
		pass


if __name__ == '__main__':
    socketio.run(app, debug=True)
