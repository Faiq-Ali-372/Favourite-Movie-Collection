from flask_sqlalchemy import SQLAlchemy

# Init the DB
db = SQLAlchemy()

# Class to hold all the movie properties
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String(150), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False, unique=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(150), nullable=True)
    img_url = db.Column(db.String, nullable=False)