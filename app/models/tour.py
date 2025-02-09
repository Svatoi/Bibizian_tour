from app import db
from app.models.utils import ModelMixin

class Tour(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    # duration = db.Column(db.Integer, nullable=False),
    # image_url = db.Column(db.String(200), nullable=False),