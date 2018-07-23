from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    lat = StringField('Lat', validators=[InputRequired()])
    lon = StringField('Lon', validators=[InputRequired()])
