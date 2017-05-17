""" 
    PlantHAT - the modular plant monitoring and growth automation system based on the RaspberryPi

        This is a Raspberry Pi HAT that allows you to turn your Pi into an plant growth automation system.
        It allows you to control watering pumps, magnetic valves, sensors and light.
        It is build with the flask microframework and provides a Admin Dashboard (sb-admin v2) with charts
        that plot your sensor data to monitor plants.
        In the strategy tab you can set up growth strategies for your plants.

        TODO:
        If you connect a RaspberryPi camera you can use the Plantix API developed by PEAT (PEAT GmbH, Hannover)
        to provide you with high class, state of the art plant disease and pests detection.
        Go and check out their website at wwww.peat.ai or test their App Plantix.

        PlantHAT on GitHub: https://github.com/MrGnomes/plantHAT

        :copyright: (c) 2017 Patrick Laza.
        :license: MIT, see LICENSE for more details.
"""

from flask import Flask
from settings import config

# Import blueprints
from app import (errors, home, auth, dashboard)

# Import extensions
from extensions import (
    db,
    bcrypt,
    login_manager,
    bootstrap,
)

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# App Factory Pattern
def create_app(config_name):
   
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    
    db.init_app(app)

    # The current app is now known. Create the database
    with app.app_context():
        db.create_all()

    bootstrap.init_app(app)
    login_manager.init_app(app)
    
    return None


def register_blueprints(app):
    
    app.register_blueprint(home.views.homeBlueprint)
    app.register_blueprint(errors.views.errorsBlueprint)
    app.register_blueprint(auth.views.authBlueprint)
    app.register_blueprint(dashboard.views.dashboardBlueprint)
    return None