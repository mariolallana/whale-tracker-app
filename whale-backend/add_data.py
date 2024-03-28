from datetime import datetime
from app import app, db
from app.models import Species, MigrationRoute, Sighting

def add_species_and_data():
    with app.app_context():
        # Define all species data including descriptions, conservation status, and routes
        species_data = [
            {
                "name": "Humpback Whale",
                "description": "Large whale known for its impressive breaching.",
                "conservation_status": "Least Concern",
                "routes": [
                    {"start_lat": -60, "start_long": 2, "end_lat": -18, "end_long": 147, "time_of_year": "May to September"}
                ],
                "sightings": [
                    {"latitude": -18.156, "longitude": 147.485, "date": datetime(2023, 3, 15), "observer": "Marine Explorer"}
                ]
            },
            {
                "name": "Blue Whale",
                "description": "The largest animal ever known to have existed.",
                "conservation_status": "Endangered",
                "routes": [
                    {"start_lat": 35, "start_long": -123, "end_lat": 23, "end_long": -112, "time_of_year": "April to October"}
                ],
                "sightings": [
                    {"latitude": 24, "longitude": -117, "date": datetime(2023, 4, 20), "observer": "Ocean Watch"}
                ]
            },
            {
                "name": "Orca",
                "description": "Also known as the killer whale, despite being a dolphin.",
                "conservation_status": "Data Deficient",
                "routes": [
                    {"start_lat": 48, "start_long": -123, "end_lat": 60, "end_long": -172, "time_of_year": "June to November"}
                ],
                "sightings": [
                    {"latitude": 54, "longitude": -160, "date": datetime(2023, 5, 25), "observer": "Whale Watcher"}
                ]
            }
        ]

        # Process each species
        for spec in species_data:
            species = Species.query.filter_by(name=spec["name"]).first()
            if not species:
                species = Species(name=spec["name"], description=spec["description"], conservation_status=spec["conservation_status"])
                db.session.add(species)
                db.session.commit()

            # Add routes
            #for route in spec["routes"]:
            #    new_route = MigrationRoute(species_id=species.id, **route)
            #    db.session.add(new_route)

            # Add sightings
            for sighting in spec["sightings"]:
                new_sighting = Sighting(species_id=species.id, **sighting)
                db.session.add(new_sighting)

        db.session.commit()
        print("Species, routes, and sightings added successfully.")

if __name__ == "__main__":
    add_species_and_data()
