from flask import Blueprint

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/')
def admin_index():
    return "I am admin_index"
