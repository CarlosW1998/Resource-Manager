from app import app
from flask import render_template

@app.route('/login')
def login():
    
    return render_template('login.html')

@app.route('/signup')
def signup():
    return 'Signup'

@app.route('/logout')
def logout():
    return 'Logout'