from flask import Blueprint

bp = Blueprint("qa", __name__, url_prefix="/qa")


@bp.route("/")
def index():
    pass