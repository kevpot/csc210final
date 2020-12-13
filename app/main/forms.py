from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, validators, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, InputRequired, NumberRange


class PlayerForm(FlaskForm):
    first_name = StringField('First Name', [validators.DataRequired(), 
        validators.Length(min=1, max=100, message='Name length between 1 and 99')])
    middle_initial = StringField('Middle Initial', [validators.Optional(), 
        validators.Length(min=1, max=1, message='Only one character for initial')])
    last_name = StringField('Last Name', [validators.DataRequired(), 
        validators.Length(min=1, max=100, message='Name length between 1 and 99')])
    date_of_birth = DateField('Date of Birth (mm/dd/yyyy)', format='%m/%d/%Y')
    age = IntegerField('Age', [validators.DataRequired()])
    home_town = StringField('Home Town', [validators.Optional(), 
        validators.Length(min=1, max=100, message='Home town length between 1 and 99')])
    height = IntegerField('Height (in.)', [validators.DataRequired()])
    weight = IntegerField('Weight (lb.)', [validators.DataRequired()])
    submit = SubmitField('Add Player')

