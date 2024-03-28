from app import app, db
from app.models import Species, MigrationRoute

# Define dummy migration data for each species for each month
# The data consists of start and end latitude/longitude to simulate migration patterns
dummy_migration_data = {
    'Orca': [
        {'start_lat': 60, 'start_long': -160, 'end_lat': 58, 'end_long': -150},  # January
        {'start_lat': 58, 'start_long': -150, 'end_lat': 56, 'end_long': -140},  # February
        {'start_lat': 56, 'start_long': -140, 'end_lat': 54, 'end_long': -130},  # March
        {'start_lat': 54, 'start_long': -130, 'end_lat': 52, 'end_long': -120},  # April
        {'start_lat': 52, 'start_long': -120, 'end_lat': 50, 'end_long': -110},  # May
        {'start_lat': 50, 'start_long': -110, 'end_lat': 48, 'end_long': -100},  # June
        {'start_lat': 48, 'start_long': -100, 'end_lat': 50, 'end_long': -110},  # July
        {'start_lat': 50, 'start_long': -110, 'end_lat': 52, 'end_long': -120},  # August
        {'start_lat': 52, 'start_long': -120, 'end_lat': 54, 'end_long': -130},  # September
        {'start_lat': 54, 'start_long': -130, 'end_lat': 56, 'end_long': -140},  # October
        {'start_lat': 56, 'start_long': -140, 'end_lat': 58, 'end_long': -150},  # November
        {'start_lat': 58, 'start_long': -150, 'end_lat': 60, 'end_long': -160},  # December
    ],
    'Humpback Whale': [
        {'start_lat': -30, 'start_long': 150, 'end_lat': -20, 'end_long': 145},  # January
        {'start_lat': -20, 'start_long': 145, 'end_lat': -10, 'end_long': 140},  # February
        {'start_lat': -10, 'start_long': 140, 'end_lat': 0, 'end_long': 135},    # March
        {'start_lat': 0, 'start_long': 135, 'end_lat': 10, 'end_long': 130},     # April
        {'start_lat': 10, 'start_long': 130, 'end_lat': 20, 'end_long': 125},    # May
        {'start_lat': 20, 'start_long': 125, 'end_lat': 30, 'end_long': 120},    # June
        {'start_lat': 30, 'start_long': 120, 'end_lat': 20, 'end_long': 125},    # July
        {'start_lat': 20, 'start_long': 125, 'end_lat': 10, 'end_long': 130},    # August
        {'start_lat': 10, 'start_long': 130, 'end_lat': 0, 'end_long': 135},     # September
        {'start_lat': 0, 'start_long': 135, 'end_lat': -10, 'end_long': 140},    # October
        {'start_lat': -10, 'start_long': 140, 'end_lat': -20, 'end_long': 145},  # November
        {'start_lat': -20, 'start_long': 145, 'end_lat': -30, 'end_long': 150},  # December
    ],
    'Blue Whale': [
        {'start_lat': 20, 'start_long': -112, 'end_lat': 15, 'end_long': -110},  # January
        {'start_lat': 15, 'start_long': -110, 'end_lat': 10, 'end_long': -108},  # February
        {'start_lat': 10, 'start_long': -108, 'end_lat': 5, 'end_long': -106},   # March
        {'start_lat': 5, 'start_long': -106, 'end_lat': 0, 'end_long': -104},    # April
        {'start_lat': 0, 'start_long': -104, 'end_lat': -5, 'end_long': -102},   # May
        {'start_lat': -5, 'start_long': -102, 'end_lat': -10, 'end_long': -100}, # June
        {'start_lat': -10, 'start_long': -100, 'end_lat': -5, 'end_long': -102}, # July
        {'start_lat': -5, 'start_long': -102, 'end_lat': 0, 'end_long': -104},   # August
        {'start_lat': 0, 'start_long': -104, 'end_lat': 5, 'end_long': -106},    # September
        {'start_lat': 5, 'start_long': -106, 'end_lat': 10, 'end_long': -108},   # October
        {'start_lat': 10, 'start_long': -108, 'end_lat': 15, 'end_long': -110},  # November
        {'start_lat': 15, 'start_long': -110, 'end_lat': 20, 'end_long': -112},  # December
    ],
}

def insert_migration_routes():
    for species_name, monthly_routes in dummy_migration_data.items():
        species = Species.query.filter_by(name=species_name).first()
        if not species:
            print(f"Species {species_name} not found in the database.")
            continue

        for month, route_data in enumerate(monthly_routes, start=1):
            route = MigrationRoute(
                species_id=species.id,
                start_lat=route_data['start_lat'],
                start_long=route_data['start_long'],
                end_lat=route_data['end_lat'],
                end_long=route_data['end_long'],
                time_of_year=month,
            )
            db.session.add(route)
        db.session.commit()
        print(f"Inserted migration routes for {species_name}.")

if __name__ == "__main__":
    with app.app_context():
        insert_migration_routes()
