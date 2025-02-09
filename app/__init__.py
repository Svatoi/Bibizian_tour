import os
from flask import Flask, render_template
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv
load_dotenv()

login_manager = LoginManager()
db = SQLAlchemy(session_options={"autoflush": False})
    
def create_app(environment="development"):
    from config import config
    from .views import main_bp, booking_bp, auth_bp
    from .models import User, AnonymousUser

    app = Flask(__name__)
    CORS(app)

    env = os.getenv("FLASK_ENV", environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    db.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(booking_bp)

    @login_manager.user_loader
    def get_user(id):
        return User.query.get(int(id))
    
    login_manager.login_view = 'auth.signin'
    login_manager.login_message_category = 'info'
    login_manager.anonymous_user = AnonymousUser

    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template("error.html", error=exc), exc.code
    
    return app