# Install Instructions

#### Requires: python, python-devel, sqlite3, pip, npm, and virtualenv

* Clone locally
* ``` $ cd teltechProj ```
* ``` $ virtualenv venv ```
* ``` $ source venv/bin/activate ```
* ``` $ pip install -r requirements.txt ```
* ``` $ python -c "from models import db; db.create_all()" ```
* ``` $ npm install ```
* ``` $ gulp ```
* ``` $ python app.py ```
* navigate to ```localhost:5000``` or ```localhost:5000/chat```

#### To load sample data

* ``` $ cd db/ ```
* ``` $ sqlite3 production.db ```
* ``` > .mode csv ```
* ``` > .import users.csv User ```
* ``` > .import sessions.csv ChatSession ```
* ``` > .import messages.csv Message ```

# API Examples

#### Get a List of Chat Representatives
``` 
localhost:5000/get_reps

GET  localhost:5000/get_reps
[
  {
    "username": "aedan",
    "userID": 1,
    "email": "aedan@company.com"
  },
  ...
]
```

#### Update Name of Chat Representative
``` 
localhost:5000/change_rep?repID=<userID>&new_name=<string>

PUT localhost:5000/change_rep?repID=1&new_name=matt
{
  "old name": "aedan",
  "username": "matt"
}
```

#### Get a List of Prior Conversations (Rep ID optional)
``` 
localhost:5000/get_sessions[?repID=<userID>]

GET localhost:5000/get_sessions?repID=1
[
  {
    "participant1": 2,
    "sessionID": 1,
    "start time UTC": "2016-11-28 18:34:57.411892",
    "participant2": 1
  },
  {
    "participant1": 1,
    "sessionID": 2,
    "start time UTC": "2016-11-28 18:35:24.490708",
    "participant2": 6
  }
]

GET localhost:5000/get_sessions
[
  ...
  {
    "participant1": 4,
    "sessionID": 3,
    "start time UTC": "2016-11-28 18:36:31.298323",
    "participant2": 3
  },
  {
    "participant1": 5,
    "sessionID": 5,
    "start time UTC": "2016-11-28 18:37:55.945724",
    "participant2": 6
  },
  ...
]
```

#### Get Messages with a Conversation Identifier
```
localhost:5000/get_messages?sessionID=<sessionID>

GET localhost:5000/get_messages?sessionID=5
[
  {
    "sessionID": 5,
    "userID": 5,
    "message": "hey",
    "timestamp UTC": "2016-11-28 18:38:08.146628"
  },
  {
    "sessionID": 5,
    "userID": 6,
    "message": "hi ed",
    "timestamp UTC": "2016-11-28 18:38:11.760586"
  },
  {
    "sessionID": 5,
    "userID": 5,
    "message": "bye eric",
    "timestamp UTC": "2016-11-28 18:38:17.953296"
  }
]
```

#### Delete a Conversation by Conversation Identifier
```
localhost:5000/delete_session?sessionID=<sessionID>

DELETE localhost:5000/delete_session?sessionID=5
{
  "deleted session ID": 5,
  "deleted messages": [
    {
      "sessionID": 5,
      "userID": 5,
      "message": "hey",
      "timestamp UTC": "2016-11-28 18:38:08.146628"
    },
    {
      "sessionID": 5,
      "userID": 6,
      "message": "hi ed",
      "timestamp UTC": "2016-11-28 18:38:11.760586"
    },
    {
      "sessionID": 5,
      "userID": 5,
      "message": "bye eric",
      "timestamp UTC": "2016-11-28 18:38:17.953296"
    }
  ]
}
```
