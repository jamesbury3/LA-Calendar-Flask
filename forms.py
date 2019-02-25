from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SubmitField, DateField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class SearchForm(FlaskForm):
    la_name = StringField('Search Your Name (Enter exactly as you did on the google form, if no times show up, you entered it incorrectly)', validators=[Length(min=0, max=30)])
    submit = SubmitField('Search')