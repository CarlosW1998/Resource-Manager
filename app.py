from flask import Flask
from flask_sqlalchemy import SQLAlchemy, _app_ctx_stack
from sqlalchemy.orm import scoped_session
import os
from config.database import Base, engine, seasson_local
from dotenv import load_dotenv
from distutils.util import strtobool
load_dotenv()
Base.metadata.create_all(bind=engine)


app = Flask(__name__)

app.config['TESTING'] = strtobool(os.getenv('TESTING'))  
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
app.session = scoped_session(seasson_local, scopefunc=_app_ctx_stack.__ident_func__)

if __name__ == '__main__':
    from routes.index import *
    app.run()