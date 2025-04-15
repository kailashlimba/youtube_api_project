import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///videos.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YOUTUBE_API_KEYS = os.getenv("YOUTUBE_API_KEYS", "").split(",")
    SEARCH_QUERY = os.getenv("SEARCH_QUERY", "cricket")
    FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", 10))  # in seconds