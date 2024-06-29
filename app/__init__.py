# app/__init__.py

from flask import Flask
from app.db import db
from app.routes import bp as main_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)

    return app
