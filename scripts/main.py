import os
import logging
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_dashboard.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or os.urandom(16).hex()
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Define the route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define the route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user = User.query.filter_by(username=username, email=email).first()
        if user:
            return redirect(url_for('dashboard'))
    return render_template('login.html')

# Define the route for the dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)