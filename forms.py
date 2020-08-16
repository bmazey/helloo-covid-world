from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TestingLocationForm(FlaskForm):
    health_center_name = StringField('Health Center Name', validators=[DataRequired()])
    operated_by = StringField('Operated by', validators=[DataRequired()])
    street_address = StringField('Street Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    telephone_number = StringField('Telephone Number', validators=[DataRequired()])
    website = StringField('Website', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
