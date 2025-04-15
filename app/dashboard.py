from flask import Blueprint, render_template, request
from app.models import Video
from sqlalchemy import or_, and_

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard():
    """
    Renders the dashboard UI with optional search and sorting.

    - Accepts query parameters:
        - 'q' for search (can be partial keywords)
        - 'sort' for sorting by published date ('asc' or 'desc')
    - Filters videos by matching all tokens in title or description.
    - Sorts the results based on the published date.
    - Renders the 'dashboard.html' template with the filtered video list.

    Returns:
        Rendered HTML page with video cards and search/sort UI.
    """
    search_query = request.args.get("q", "")
    sort_order = request.args.get("sort", "desc")

    query = Video.query

    if search_query:
        tokens = search_query.lower().split()
        filters = [
            or_(
                Video.title.ilike(f"%{token}%"),
                Video.description.ilike(f"%{token}%")
            ) for token in tokens
        ]
        query = query.filter(and_(*filters))

    if sort_order == "asc":
        query = query.order_by(Video.published_at.asc())
    else:
        query = query.order_by(Video.published_at.desc())

    videos = query.all()

    return render_template("dashboard.html", videos=videos, search_query=search_query, sort_order=sort_order)