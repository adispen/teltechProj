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

### To load sample data

* ``` $ cd db/ ```
* ``` $ sqlite3 production.db ```
* ``` > .mode csv ```
* ``` > .import users.csv User ```
* ``` > .import sessions.csv ChatSession ```
* ``` > .import messages.csv Message ```
