"""
    extensions
    ----------

    Wordaround to avoid circular dependency inside the app.
    An example of this would be the import of the 'db' field inside "app/models/user.py" .
    Since the 'auth' blueprint includes the User class from models/user.py and user.py includes the 'db' field we have a circular dependency. 
    When we initialize the app in __init__.py(app) we need to include the auth folder, before the db object is created.
    This results in an compilation error because the db object is created after the include directives. This avoids the problem by providing basic 
    uninitialized objects with just enough information to avoid a compilation error.

    Brief:
    To avoid an compilation error use this file as a global file to create a objects containing the used extensions before actually starting the app.

    :copyright: (c) 2017 Patrick Laza.
    :license: MIT, see LICENSE for more details.
"""


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from flask_login import LoginManager
login_manager = LoginManager()

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()
