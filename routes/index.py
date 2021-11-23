from app import app
from config.database import session_local
from flask import url_for, redirect

@app.route("/")
def index():
    return redirect(url_for('login'))