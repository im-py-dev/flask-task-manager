import os
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

load_dotenv()
FLASK_DEBUG = bool(os.getenv('FLASK_DEBUG', True))
if FLASK_DEBUG:
    app.config.from_object('app.config.DevelopmentConfig')
else:
    app.config.from_object('app.config.ProductionConfig')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from app.auth import auth
from app.views import views

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(views, url_prefix='/')
