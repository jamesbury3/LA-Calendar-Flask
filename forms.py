from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SubmitField, DateField, SelectField, TextField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class SearchForm(FlaskForm):
    la_name = StringField('Search Your Name (use the autocorrect):', validators=[Length(min=0, max=30)], id='name_autocomplete')
    submit = SubmitField('Search')