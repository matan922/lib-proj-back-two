import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'supersecret' #to allow us to use forms, not safe for deployment
app.config["TEMPLATES_AUTO_RELOAD"] = True
##########################################
############ DATABASE SETUP ##############
##########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, "Library_DATABASE")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
Migrate(app, db)

##########################################
######### REGISTER BLUEPRINTS ############
##########################################

from project.core.views import core
from project.books.views import books
from project.clients.views import client
from project.loans.views import loans

app.register_blueprint(client)
app.register_blueprint(core)
app.register_blueprint(books)
app.register_blueprint(loans)
