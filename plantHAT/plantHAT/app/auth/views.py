""" 
    auth.views
    ------

    Defines the views and sets the routes used in the login and the registration page.
"""

from flask import (Blueprint, render_template, redirect, request, url_for, flash,  make_response)

from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, RegistrationForm

from app.models.user  import User
from extensions import (db, login_manager)

authBlueprint = Blueprint('auth', __name__, static_folder="../static")

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('auth.login'))

@authBlueprint.route("/login", methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is not None and user.verify_password(form.password.data):
            login_user(user, False)
            return redirect(url_for('dashboard.index', username=user.username))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html', loginform=form)

@authBlueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))

@authBlueprint.route('/register', methods=['GET', 'POST'])
def register():
    
    registrationform = RegistrationForm()
    
    if registrationform.validate_on_submit():
        
        # Create the user object and set the default avatar image as the profile pic
        user = User(username=registrationform.username.data,
                    password=registrationform.password.data,
                    profileImage = url_for('static', filename='img/plantHAT_avatar.jpg'))

        
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created.')
        
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', registrationform=registrationform)
