"""Class-based Flask app configuration."""
from os import environ, path
from dotenv import load_dotenv
import secrets

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SESSION_COOKIE_NAME = secrets.token_urlsafe(32)
    SECRET_KEY = secrets.token_urlsafe(32)
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_APP = 'wsgi.py'

    print(SECRET_KEY)
    print(SESSION_COOKIE_NAME)

    # Flask Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')
    COMPRESS_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # Flask-Session
    #SESSION_TYPE = environ.get('SESSION_TYPE')
    #SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS'))

    # AWS Secrets
    AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    AWS_KEY_ID = environ.get('AWS_KEY_ID')

    # ReCaptcha Info
    RECAPTCHA_PUBLIC_KEY = environ.get('RECAPTCHA_PUB')
    RECAPTCHA_PARAMETERS = {'size': '100%'}
