from flask import Flask, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from models import User

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Placeholder for login logic
    return 'Login Page'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Placeholder for registration logic
    return 'Register Page'