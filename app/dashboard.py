from flask import Blueprint, render_template, request
from app.models import Video
from sqlalchemy import or_, and_

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard():
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