import os


basedir = os.path.abspath(os.path.dirname(__file__))


class dev(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
