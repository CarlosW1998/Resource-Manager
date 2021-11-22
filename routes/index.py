from app import app

@app.route("/")
def index():
    return "Nothing to see here"