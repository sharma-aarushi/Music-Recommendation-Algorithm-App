import sys
print(sys.executable)

from flask import Flask, render_template
from flask_login import LoginManager, UserMixin, login_required, login_user
import os

app = Flask(__name__)
app.secret_key = 'my_own_secret_key_here' #TODO: Replace with more secure key

# Simulated user data for testing
# TODO: Replace this with a real database later
users = {'testuser': {'password': 'testpassword'}}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    return User(username)

#Route for the login page and mock login function:
from flask import request, redirect, url_for

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('profile'))
    return render_template('login.html')

#Route for user profile page and mock profile function:
from flask_login import current_user

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=current_user.id)

# Set the absolute path of the 'templates' folder
template_dir = os.path.abspath('templates')
app.template_folder = template_dir
from flask import Flask, render_template

app = Flask(__name__)