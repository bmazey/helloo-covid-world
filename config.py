import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    try:
        SECRET_KEY = open("/run/secrets/key_secret", "r").read().strip()
    except Exception:
        SECRET_KEY = 'wouldnt-you-like-to-know'

    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
