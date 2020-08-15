from database import db


class TestingLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    health_center_name = db.Column(db.String(64), index=True)
    operated_by = db.Column(db.String(64), index=True)
    street_address = db.Column(db.String(64), index=True)
    city = db.Column(db.String(64), index=True)
    state = db.Column(db.String(64), index=True)
    zip_code = db.Column(db.String(64), index=True)
    telephone_number = db.Column(db.String(64), index=True)
    website = db.Column(db.String(64), index=True)
    test_status = db.Column(db.String(64), index=True)
    telehealth_status = db.Column(db.String(64), index=True)
    description = db.Column(db.String(128), index=True)

    # string representation dunder
    def __repr__(self):
        return '{{"health_center_name": "{}", "operated_by": "{}", "street_address": "{}", "city": "{}"}}'.format(self.health_center_name,self.operated_by,self.street_address,self.city)
