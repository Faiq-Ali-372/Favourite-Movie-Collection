from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

# Creating a class to add the movie
class Add(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Add Movie')