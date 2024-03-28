from app import db

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)  # New field
    conservation_status = db.Column(db.String(50), nullable=True)  # New field
    routes = db.relationship('MigrationRoute', backref='species', lazy=True)

class MigrationRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)
    start_lat = db.Column(db.Float, nullable=False)
    start_long = db.Column(db.Float, nullable=False)
    end_lat = db.Column(db.Float, nullable=False)
    end_long = db.Column(db.Float, nullable=False)
    time_of_year = db.Column(db.Integer, nullable=False)  # New field

class Sighting(db.Model):  # New model
    id = db.Column(db.Integer, primary_key=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    observer = db.Column(db.String(100), nullable=True)  # Optional
