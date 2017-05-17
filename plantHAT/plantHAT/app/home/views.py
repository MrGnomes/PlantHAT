""" 
    home.views
    ------

    Home Screen when visiting the plantHAT server.
"""

from flask import (Blueprint, render_template)

homeBlueprint = Blueprint('home', __name__)

@homeBlueprint.route('/')
def index():
    return render_template('home/index.html')

@homeBlueprint.route("/about/")
def about():
    return render_template("home/about.html")

