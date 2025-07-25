from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS
import os

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def createApp():
    load_dotenv()

    app = Flask(__name__)

    env = os.getenv('development')
    if env == 'production':
        from app.config import ProdConfig
        app.config.from_object(ProdConfig)
    elif env == 'testing':
        from app.config import TestConfig
        app.config.from_object(TestConfig)
    else:
        from app.config import DevConfig
        app.config.from_object(DevConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    from app.routes.saludo import bp_saludo
    app.register_blueprint(bp_saludo, url_prefix='/api')

    return app