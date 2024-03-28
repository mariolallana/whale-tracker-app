from app import app, db  # Ensure whaleback is the correct import path for your Flask app instance and db
from app.models import Species, MigrationRoute  # Adjust the import path if necessary

def create_database():
    with app.app_context():  # This line creates the application context
        print("Creating database tables...")
        db.drop_all()  # Drops existing tables, remove if you want to keep the data
        db.create_all()  # Creates tables based on your SQLAlchemy models
        print("Database tables created.")

if __name__ == "__main__":
    create_database()
