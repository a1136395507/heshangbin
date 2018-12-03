import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR,'static/img/')


class Baseconfig():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'kufrq*gr&#hfhafkjakkakHKJHFKAHSDJ'

class DevelopConfig(Baseconfig):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' +os.path.join(BASE_DIR,'develop.db')





config = {
    'develop':DevelopConfig,
    'default':DevelopConfig,
}

def init_cogfig(app,env_name):
    app.config.from_object(config.get(env_name or 'default'))