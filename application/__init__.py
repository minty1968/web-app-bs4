"""Initialize app."""
#from application.common.assets import compile_static_assets
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
#from ddtrace import patch_all

# Globally accessible libraries
#patch_all()
db = SQLAlchemy()
lm = LoginManager()
sess = Session()

def create_app():
    """Construct the core application."""
    # Application Configuration
    app = Flask(__name__, instance_relative_config=False)
    csrf = CSRFProtect(app)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config.from_object('config.Config')
    
    # Initialize Plugins
    db.init_app(app)
    lm.init_app(app)
    csrf.init_app(app)
    sess.init_app(app)
    
    with app.app_context():
        # Import parts of our application
        from application.views.base import baseBP
        from application.views.forms import formsBP
        from application.views.lottery import lotteryBP
        from application.views.password import passwdBP
        from application.views.games import gameBP

        # Register Blueprints
        app.register_blueprint(baseBP)
        app.register_blueprint(formsBP)
        app.register_blueprint(lotteryBP)
        app.register_blueprint(passwdBP)
        app.register_blueprint(gameBP)
    
        # Create Database Models
        # db.create_all()

        # Compile static assets
        #if app.config['FLASK_ENV'] == 'development':
        #    compile_static_assets(app) 

        return app
