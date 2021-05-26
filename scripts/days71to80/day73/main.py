from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import desc
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

API_KEY = os.environ.get('MOVIE_DB_API_KEY')

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-10-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

class EditForm(FlaskForm):
    rating = FloatField("Your rating out of 10")
    review = StringField("Your review")
    submit = SubmitField("Done")

class AddMovie(FlaskForm):
    name = StringField("Movie title")
    submit = SubmitField("Add Movie")

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(1000), nullable=False)


db.create_all()


# new_movie = Movies(
#     title="What we do in the shadows",
#     year = 2014,
#     description = "Viago, Deacon and Vladislav are vampires who are finding that modern life has them struggling with the mundane - like paying rent, keeping up with the chore wheel, trying to get into nightclubs and overcoming flatmate conflicts.",
#     rating = 9,
#     ranking = 2,
#     review = "Amazingly funny and dark all at once",
#     img_url = "https://worldoftaika.files.wordpress.com/2013/12/official-poster-no1.jpg?w=940&h=658"
# )
#
# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    all_movies = Movies.query.order_by(Movies.rating.desc()).all()
    order = 1
    for i in range(len(all_movies)):
        all_movies[i].ranking = order
        order += 1
    db.session.commit()

    return render_template("index.html", movie_list=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_name = form.name.data
        data = requests.get(url=MOVIE_DB_SEARCH_URL, params={"api_key": API_KEY, "query": movie_name})
        movie_data = data.json()["results"]
        return render_template("select.html", options=movie_data)
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    movie = Movies.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete", methods=["GET"])
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movies.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movies(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            description=data["overview"],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("edit", id=new_movie.id))
    

if __name__ == '__main__':
    app.run(debug=True)
