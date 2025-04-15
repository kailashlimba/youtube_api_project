from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Creating DB 
class Video(db.Model):
    id = db.Column(db.String, primary_key=True)  # YouTube Video ID
    title = db.Column(db.String, index=True)
    description = db.Column(db.Text, index=True)
    published_at = db.Column(db.DateTime, index=True)
    thumbnail_url = db.Column(db.String)

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "published_at": self.published_at.isoformat(),
            "thumbnail_url": self.thumbnail_url
        }