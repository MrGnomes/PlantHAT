""" 
    errors.views
    ------

    Error Handler for the standard HTTP Errors.
    When a error is detected, the HTML-Site from the templates folder gets rendered

"""

from flask import (Blueprint, render_template)

errorsBlueprint = Blueprint('errors', __name__)

@errorsBlueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@errorsBlueprint.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500