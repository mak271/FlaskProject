from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class EmployerForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    surname = StringField('Surname', validators = [DataRequired()])
    age = IntegerField('Age', validators = [DataRequired()])
    date_employment = DateField('Date of employment', format="%Y-%m-%d")
    submit = SubmitField('Save')