import json
from flask import Blueprint
from models import TestingLocation

pages = Blueprint('pages', __name__)


@pages.route('/testing/locations', methods=['GET'])
def get_all_locations():
    locations = TestingLocation.query.all()
    return str(locations)


@pages.route('/testing/locations/<zip_code>', methods=['GET'])
def get_locations_by_zip_code(zip_code):
    locations = TestingLocation.query.filter_by(zip_code=zip_code).all()
    return str(locations)

