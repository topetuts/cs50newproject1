import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'topetuts'

    SQLALCHEMY_DATABASE_URI = 'mysql://topetuts:s76zkY5pqu@topetuts.mysql.pythonanywhere-services.com/topetuts$project1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


