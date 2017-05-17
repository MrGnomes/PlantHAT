"""
    settings
    ________

    Global app settings. It defines the 3 possible configurations that can be used for this app:
        Development, with debugging options turned on
        Testing, with the unit testing option turned on
        Production, which is the final app.

        The configuration can be selected in the run.py file, 
        by selecting the desired configuration string defined at the end of this file in the
        create_app() factory pattern function.

        :copyright: (c) 2017 Patrick Laza.
        :license: MIT, see LICENSE for more details.
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '\\xaf\\x93]\\xe8\\x07a\\xd3\\xc4O\\x0f\\x7f\\x0e\\x80\\x02J\\x7f\\xa0\\xf0/R.Zo\\x88'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data', 'dev.db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data', 'test.db')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data', 'plantHAT.db')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}