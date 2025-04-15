from flask import Flask
from app.models import db
from app.routes import bp as api_bp
from app.scheduler import start_scheduler
from app.dashboard import dashboard_bp
from config import Config

def create_app():
    """
    Creates and configures the Flask application.

    - Loads configuration from the Config class.
    - Initializes the database with SQLAlchemy.
    - Registers API and dashboard blueprints.
    - Creates database tables if they don't exist.
    - Starts the background scheduler to fetch YouTube videos periodically.

    Returns:
        app (Flask): The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(api_bp)
    app.register_blueprint(dashboard_bp)

    with app.app_context():
        db.create_all()
        start_scheduler(app)

    return app
