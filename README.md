# YouTube Video Fetcher API

This project is a Flask-based API to fetch the latest YouTube videos for a given search query and store them in a database. It provides:
- A paginated API to view videos
- A smart search API with partial match support
- A simple dashboard UI to browse videos with filters and sorting

---

## Features

- Background worker to fetch videos from YouTube every 10 seconds
- Stores videos with title, description, thumbnail, and publish time
- Search API with partial matching (Bonus)
- Dashboard UI with filter and sort (Bonus)
- Fully Dockerized for easy deployment
- Supports multiple YouTube API keys (Bonus)

---

## Tech Stack

- Python 3.9
- Flask
- SQLAlchemy
- APScheduler
- Docker + Docker Compose

---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/username/youtube_api_project.git
cd youtube_api_project
```

---

### 2. Add Your YouTube API Key(s)

Open the `docker-compose.yml` file and update the environment section:

```yaml
environment:
  YOUTUBE_API_KEYS: "your_api_key"
  SEARCH_QUERY: "cricket"
  FETCH_INTERVAL: "10"
```

You can add multiple API keys separated by commas.

---

### 3. Run the Project Using Docker

```bash
docker-compose build
docker-compose up
```

The app will be available at:  
 `http://localhost:5000/`

---

##  API Endpoints

### `GET /videos`

Returns a paginated list of videos.

- `page`: Page number (default: 1)  
- `per_page`: Number of videos per page (default: 10)

---

### `GET /search`

Searches videos by title and description using all keywords (partial).

- `q`: Search query  
- `page`: Page number  
- `per_page`: Number of results per page

---

##  Dashboard

Visit: `http://localhost:5000/` in your browser.

You can:
- Filter videos using keywords  
- Sort by published date (newest/oldest)  
- See video thumbnails and basic info

---

##  Notes

- Make sure your YouTube API key has **YouTube Data API v3** enabled.
- If the quota is exceeded for one key, the app will automatically try the next one if provided.
