import os

class Config:
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('URI_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI = os.getenv('URI_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('URI_DATABASE')