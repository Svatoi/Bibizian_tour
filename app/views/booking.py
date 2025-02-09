from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required, logout_user

from app.models import Booking

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/book/<int:tour_id>', methods=['GET', 'POST'])
def book_tour(tour_id):
    if request.method == 'POST':
        name = request.form.get['name']
        email = request.form.get['email']
        
        booking = Booking(
            tour_id=tour_id, 
            name=name, 
            email=email
        )
        booking.save()
        
        return redirect(url_for('index'))
    return render_template("booking.html", tour_id=tour_id)