from app import app
from config.database import session_local

@app.route("/")
def index():
    return "Nothing to see here"