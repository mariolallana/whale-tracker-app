from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config  # Import the Config class

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)  # Apply configurations
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
