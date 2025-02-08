from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    farm = db.Column(db.String(100), nullable=False)
    cod = db.Column(db.String(10), nullable=False)
    series_number = db.Column(db.String(20), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    is_lactating = db.Column(db.Boolean, default=False)
    calving_history = db.Column(db.JSON, default=[])  # Historial de partos