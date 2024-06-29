# config.py

import os

class Config:
    DEBUG = True  # Modo debug activado
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:admin@localhost/people'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
