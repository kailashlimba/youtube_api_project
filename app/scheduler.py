from apscheduler.schedulers.background import BackgroundScheduler
from app.youtube import fetch_videos

def start_scheduler(app):
    """
    Starts a background scheduler that runs the YouTube video fetch job
    at regular intervals defined by the FETCH_INTERVAL config.

    - Uses APScheduler to schedule the fetch_videos() task.
    - Wraps the job inside app.app_context() to ensure access to Flask context.
    - The job is triggered repeatedly based on the interval in seconds.

    Args:
        app (Flask): The Flask application instance.
    """
    scheduler = BackgroundScheduler()

    def job_wrapper():
        with app.app_context():
            fetch_videos()

    scheduler.add_job(func=job_wrapper, trigger="interval", seconds=app.config["FETCH_INTERVAL"])
    scheduler.start()