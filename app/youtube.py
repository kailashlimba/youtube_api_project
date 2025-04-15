import requests
from datetime import datetime, timedelta
from app.models import Video, db
from flask import current_app

def fetch_videos():
    """
    Fetches the latest videos from YouTube based on the configured search query.

    - Loops through available API keys to handle quota limits.
    - Uses YouTube Data API v3 to retrieve videos sorted by publish date.
    - Filters out duplicate videos using their YouTube video ID.
    - Saves only new videos to the database.
    
    """
    keys = current_app.config["YOUTUBE_API_KEYS"]
    search_query = current_app.config["SEARCH_QUERY"]
    published_after = (datetime.utcnow() - timedelta(seconds=current_app.config["FETCH_INTERVAL"])).isoformat("T") + "Z"

    for key in keys:
        url = f"https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "q": search_query,
            "type": "video",
            "order": "date",
            # "publishedAfter": published_after,
            "key": key,
            "maxResults": 10
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for item in data.get("items", []):
                vid = item["id"]["videoId"]
                snippet = item["snippet"]
                if not Video.query.get(vid):
                    video = Video(
                        id=vid,
                        title=snippet["title"],
                        description=snippet["description"],
                        published_at=datetime.strptime(snippet["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"),
                        thumbnail_url=snippet["thumbnails"]["high"]["url"]
                    )
                    db.session.add(video)
            db.session.commit()
            break
