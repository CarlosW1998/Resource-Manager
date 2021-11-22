from flask import Flask


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

if __name__ == '__main__':
    from routes.index import *
    app.run()