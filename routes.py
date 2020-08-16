import json
from flask import Blueprint, render_template

from database import db
from forms import TestingLocationForm
from models import TestingLocation

pages = Blueprint('pages', __name__)


@pages.route('/', methods=['GET'])
def hello():
    return 'hello COVID world'


@pages.route('/testing/location', methods=['GET', 'POST'])
def create_new_location():
    form = TestingLocationForm()
    if form.validate_on_submit():
        location = TestingLocation(health_center_name=form.health_center_name.data,
                                   operated_by=form.operated_by.data,
                                   street_address=form.street_address.data,
                                   city=form.city.data,
                                   state=form.state.data,
                                   zip_code=form.zip_code.data,
                                   telephone_number=form.telephone_number.data,
                                   website=form.website.data,
                                   test_status="Yes",
                                   telehealth_status="Yes",
                                   description=form.description.data)
        if TestingLocation.query.filter_by(health_center_name=form.health_center_name.data).first() is not None:
            return render_template('register.html', title='Register', form=form)
        db.session.add(location)
        db.session.commit()
        return render_template('register.html', title='Register', form=form)
    return render_template('register.html', title='Register', form=form)



@pages.route('/testing/locations', methods=['GET'])
def get_all_locations():
    locations = TestingLocation.query.all()
    return str(locations)


@pages.route('/testing/locations/zip/<zip_code>', methods=['GET'])
def get_locations_by_zip_code(zip_code):
    locations = TestingLocation.query.filter_by(zip_code=zip_code).all()
    return str(locations)


@pages.route('/testing/locations/state/<state>', methods=['GET'])
def get_locations_by_state(state):
    locations = TestingLocation.query.filter_by(state=state).all()
    return str(locations)




