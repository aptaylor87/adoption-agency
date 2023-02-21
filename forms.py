from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Email, Optional, NumberRange, URL



class PetForm(FlaskForm):
    """Form for adding and editing pets"""
    name = StringField("Pet Name", validators=[InputRequired(message="Name can't be blank")])
    species = SelectField("Species", choices=[
        ('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="Must be a URL")])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message='Age must be between 0 and 30')])
    notes = StringField("Notes")
    available = BooleanField("Available")

