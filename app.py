from flask import Flask

from config import Config
from database import db
from models import TestingLocation
from routes import pages


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        # register a test location automatically
        try:
            location = TestingLocation(
                health_center_name='Very Important Health Center',
                operated_by='Very Qualified Health Council',
                street_address='123 Sunset Street',
                city='Chicago',
                state='IL',
                zip_code='60411',
                telephone_number='606-334-9714',
                website='http://www.veryimportanthealthcenter.org',
                test_status='Yes',
                telehealth_status='Yes',
                description='As of 08/07/2020, this health center reported providing COVID-19 testing and services via '
                            'telehealth at one or more sites. Please call the center for more information.',
            )

            db.session.add(location)
            db.session.commit()

            location = TestingLocation(
                health_center_name='Other Important Health Center',
                operated_by='Other Qualified Health Council',
                street_address='123 Sunset Street',
                city='Chicago',
                state='IL',
                zip_code='60411',
                telephone_number='606-334-9714',
                website='http://www.veryimportanthealthcenter.org',
                test_status='Yes',
                telehealth_status='Yes',
                description='As of 08/07/2020, this health center reported providing COVID-19 testing and services via '
                            'telehealth at one or more sites. Please call the center for more information.',
            )

            db.session.add(location)
            db.session.commit()

        except Exception:
            pass

        # routing blueprint
        app.register_blueprint(pages)

        return app


if __name__ == '__main__':
    app = create_app()
    app.run()
