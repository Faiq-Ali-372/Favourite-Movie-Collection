from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

# Creating a class to update the details
class Update(FlaskForm):
    rating = StringField('Your rating out of 10 e.g 8.5', validators=[DataRequired(), Length(max=4)])
    review = StringField('Your review', validators=[DataRequired(), Length(max=150)])
    submit = SubmitField('Done')