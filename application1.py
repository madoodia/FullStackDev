# --------------------- #
# (C) 2021 madoodia.com #
# --------------------- #

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.title}:{self.year}"


@app.route("/")
def index():
    return "Hello world!"


@app.route("/movies")
def get_movies():
    movies = Movie.query.all()
    data = []
    for movie in movies:
        data.append({"title": movie.title, "year": movie.year})

    return {"Movies": data}


# ------------------
if __name__ == "__main__":
    # creating database if the program be launched directly
    db.create_all()
    db.session.add(Movie(title="Gladiator", year=2000))
    db.session.commit()
    db.session.add(Movie(title="Seven", year=1998))
    db.session.commit()
