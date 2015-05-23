from flask.ext.sqlalchemy import SQLAlchemy
from flask_zurb_foundation import Foundation

from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.stormpath import StormpathManager

stormpath = StormpathManager()
db = SQLAlchemy()
foundation = Foundation()
toolbar = DebugToolbarExtension()