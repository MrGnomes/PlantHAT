""" 
    models.user
    ------

    User model used by the app and stored in an sqlite database.
"""

from flask_login import UserMixin

from extensions import (db, bcrypt, login_manager )

class User(UserMixin, db.Model):
    """ 
    Defines the user model used by the plantHAT App 
    by using an database id, a username and a password hashed by bcrypt.
    """ 
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    profileImage = db.Column(db.String(128))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.username


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash =  bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

