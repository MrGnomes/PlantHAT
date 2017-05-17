""" 
    dashboard.views
    ------

    This is the admin dashboard of the plantHAT.
    It's the main view, from where on everything regarding the plant growth/watering can be monitored and controlled.
"""

from flask import (Blueprint, render_template, make_response)
from flask_login import login_required, current_user

dashboardBlueprint = Blueprint('dashboard', __name__)

@dashboardBlueprint.route("/dashboard")
@login_required
def index():
   return render_template("dashboard/index.html", username=current_user.username, profileImage=current_user.profileImage)

@dashboardBlueprint.route("/daily")
@login_required
def daily():
	return render_template("dashboard/daily.html", username=current_user.username, profileImage=current_user.profileImage)

@dashboardBlueprint.route("/monthly")
@login_required
def monthly():
	return render_template("dashboard/monthly.html", username=current_user.username, profileImage=current_user.profileImage)

@dashboardBlueprint.route("/yearly")
@login_required
def yearly():
	return render_template("dashboard/yearly.html", username=current_user.username, profileImage=current_user.profileImage)

@dashboardBlueprint.route("/strategies")
@login_required
def strategies():
	return render_template("dashboard/strategies.html", username=current_user.username, profileImage=current_user.profileImage)

