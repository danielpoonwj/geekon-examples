from flask import Flask

flask_app = Flask(__name__)

from demo_app.routes import flask_app
