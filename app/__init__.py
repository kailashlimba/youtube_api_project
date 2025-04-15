from flask import Flask
from app.models import db
from app.routes import bp as api_bp
from app.scheduler import start_scheduler
from app.dashboard import dashboard_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(api_bp)
    app.register_blueprint(dashboard_bp)

    with app.app_context():
        db.create_all()
        start_scheduler(app)

    return app
