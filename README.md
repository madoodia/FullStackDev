# FullStackDev

Learning Some concepts of Full Stack Development

USAGE: (All codes are on Windows 10 OS)

- create venv

  - $ python -m venv .venv
  - $ .venv\Scripts\activate

- install needed packages

  - $ pip install requests
  - $ pip install flask
  - $ pip install flask-sqlalchemy

- for having package requirements we use this command to keep them
  - $ pip freeze > requirements.txt

---

- writing RESTfull API with flask (and database with SQLAlchemy)

  - define environment varibales: (powershell)
    - $ $env:FLASK_APP="application1.py"
    - $ $env:FLASK_ENV="development"
  - after writing code, should run the server:
    - $ flask run

- writing RESTfull API with django
  - define environment varibales: (powershell)
    - $ $env:FLASK_APP="application2.py"
    - $ $env:FLASK_ENV="development"
  - after writing code, should run the server:
    - $ flask run
