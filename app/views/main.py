from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required, logout_user

from app.models import Tour

main_bp = Blueprint("main", __name__)

@main_bp.route('/')
def index():
    tours = Tour.query.all()
    return render_template('index.html', tours=tours)

@main_bp.route('/tour/<int:tour_id>', methods=['GET', 'POST'])
def tour_detail(tour_id):
    tour = Tour.query.get_or_404(tour_id)
    return render_template('tour.html', tour=tour)