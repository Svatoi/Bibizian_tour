from app import db
from datetime import datetime
from app.models.utils import ModelMixin

class Booking(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.Date, default=datetime.now)
    quantity = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    
    user = db.relationship('User', back_populates='booking')