from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
# My Files
from Class.myMovies import Movies, db
from Forms.updateForm import Update
from Forms.addForm import Add
from API.get_movie_data import get_movie


app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Top_10_Movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Lwi4u84@,er4r4w' # CSRF Token
# Initializing the CSRF protection
csrf = CSRFProtect(app)
# Initalizing the bootstrap
bootstrap = Bootstrap(app)
# Initialize SQLAlchemy with Flask application
db.init_app(app)

# Homepage
@app.route("/")
def home():
    # Getting all the movie properties
    all_movies = Movies.query.all()
    return render_template("index.html", movies=all_movies)


# Edit page
@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = Update()
    movie_id = request.args.get("id")
    movie_to_update = db.session.query(Movies).get(movie_id)
    # Validation
    if form.validate_on_submit() and request.method == "POST":
        movie_to_update.rating = float(form.rating.data)
        movie_to_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template(template_name_or_list="edit.html", movie=movie_to_update, form=form)


# Delete route
@app.route("/delete", methods=["GET"])
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.session.query(Movies).get(movie_id)
    # Validation
    if movie_to_delete:
        # Deleting the movie form DB
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for("home", movie=movie_to_delete))
    else:
        return "Movie not found."


# Add page
@app.route("/add", methods=["GET", "POST"])
def add():
    form = Add()
    # Validation
    if request.method == "POST" and form.validate_on_submit():
        movie_title = form.title.data
        # Making API request
        movies = get_movie(movie_title)
        return render_template(template_name_or_list="select.html", options=movies)
    return render_template(template_name_or_list="add.html", form=form)


# Find Route
@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    movie_poster_path = request.args.get("poster_img")
    movie_title = request.args.get("title")
    movie_release_date = request.args.get("release_date")
    movie_description = request.args.get("description")
    movie_ranking = float(request.args.get("ranking"))
    # Adding in DB
    new_movie = Movies(
        title=movie_title,
        year=movie_release_date.split("-")[0],
        img_url=f"https://image.tmdb.org/t/p/original{movie_poster_path}",
        description=movie_description,
        ranking=movie_ranking,
        rating=0,
        review="No review",
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("home"))


# Executing as script
if __name__ == '__main__':
    # Creating the db table
    with app.app_context():
        db.create_all()
        # Feeding the data
        # new_Movie = Movies(
        #     title="Phone Booth",
        #     year=2002,
        #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        #     rating=7.3,
        #     ranking=10,
        #     review="My favourite character was the caller.",
        #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        # )
        # db.session.add(new_Movie)
        # db.session.commit()
    # Init the app
    app.run(debug=True, host="127.0.0.1", port=5000)
