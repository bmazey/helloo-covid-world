import json
from flask import Blueprint
from models import TestingLocation

pages = Blueprint('pages', __name__)


@pages.route('/testing/locations', methods=['GET'])
def get_all_locations():
    locations = TestingLocation.query.all()
    return str(locations[0])
