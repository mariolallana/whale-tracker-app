from app import db
from app.models import MigrationRoute

# Drop the MigrationRoute table
MigrationRoute.__table__.drop(db.engine)
