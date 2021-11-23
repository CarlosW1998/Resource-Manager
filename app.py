from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy, _app_ctx_stack
from sqlalchemy.orm import backref, scoped_session
import os
from config.database import engine, session_local
from models.model import Base
from distutils.util import strtobool

Base.metadata.create_all(bind=engine)

app = Flask(__name__)

app.config['TESTING'] = strtobool(os.getenv('TESTING'))  
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
app.session = scoped_session(session_local, scopefunc=_app_ctx_stack.__ident_func__)

if __name__ == '__main__':
    from routes.index import *
    from routes.auth import *
    app.run()