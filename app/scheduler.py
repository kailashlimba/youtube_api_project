from apscheduler.schedulers.background import BackgroundScheduler
from app.youtube import fetch_videos

def start_scheduler(app):
    scheduler = BackgroundScheduler()

    def job_wrapper():
        with app.app_context():
            fetch_videos()

    scheduler.add_job(func=job_wrapper, trigger="interval", seconds=app.config["FETCH_INTERVAL"])
    scheduler.start()