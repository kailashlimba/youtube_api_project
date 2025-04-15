from flask import Blueprint, request, jsonify
from app.models import Video
from sqlalchemy import or_, and_

bp = Blueprint("api", __name__)


@bp.route("/videos", methods=["GET"])
def get_videos():
    """
    API endpoint to return a paginated list of stored YouTube videos.

    Query Parameters:
        - page (int): Page number to retrieve (default: 1)
        - per_page (int): Number of videos per page (default: 10)

    Returns:
        JSON response containing:
            - videos: List of video dictionaries
            - total: Total number of videos
            - pages: Total number of pages
            - page: Current page number
    """
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    videos = Video.query.order_by(Video.published_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        "videos": [v.as_dict() for v in videos.items],
        "total": videos.total,
        "pages": videos.pages,
        "page": videos.page
    })


@bp.route("/search", methods=["GET"])
def search_videos():
    """
    API endpoint to search videos by title or description using keyword tokens.

    Query Parameters:
        - q (str): Search query string (split into tokens)
        - page (int): Page number to retrieve (default: 1)
        - per_page (int): Number of results per page (default: 10)

    Returns:
        JSON response containing:
            - videos: List of matched videos
            - total: Total number of matched results
            - pages: Total number of pages
            - page: Current page number
    """
    query = request.args.get("q", "").strip()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))

    if not query:
        return jsonify({"videos": [], "total": 0, "pages": 0, "page": page})

    # Tokenize the search query
    tokens = query.lower().split()

    # Build dynamic filters: each token must match title or description
    filters = [
        or_(
            Video.title.ilike(f"%{token}%"),
            Video.description.ilike(f"%{token}%")
        ) for token in tokens
    ]

    # Combine all filters with AND (must match all tokens)
    search_filter = and_(*filters)

    results = Video.query.filter(search_filter).order_by(Video.published_at.desc()) \
        .paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "videos": [v.as_dict() for v in results.items],
        "total": results.total,
        "pages": results.pages,
        "page": results.page
    })