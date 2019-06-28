from loggin import DEBUG

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config_by_name[config_name])
  app.init_app(app)

  app.logger.setLevel(DEBUG)
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint, url_prefix="/")

  return app
