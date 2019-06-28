import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
  DEBUG = False

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DB_URI = 'postgresql+psycopg2:///' + os.path.join(basedir, 'db', 'courses-dev.db')

class TestingConfig(Config):
  DEBUG = True
  SQLALCHEMY_DB_URI = 'postgresql+psycopg2:///' + os.path.join(basedir, 'db', 'courses-test.db')

class ProductionConfig(Config):
  DEBUG = False
  SQLALCHEMY_DB_URI = 'postgresql+psycopg2:///' + os.path.join(basedir, 'db', 'courses.db')

config_by_name = dict(
  dev = DevelopmentConfig,
  test = TestingConfig,
  prod = ProductionConfig,
)
