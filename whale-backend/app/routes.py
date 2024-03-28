from flask import jsonify
from app import app
from app.models import Species, MigrationRoute

@app.route('/api/species', methods=['GET'])
def get_species():
    species = Species.query.all()
    return jsonify([{'id': s.id, 'name': s.name} for s in species])

@app.route('/api/species/<int:species_id>')
def get_species_by_id(species_id):
    species = Species.query.get(species_id)
    if species:
        return jsonify({'id': species.id, 
                        'name': species.name, 
                        'description': species.description, 
                        'conservation_status': species.conservation_status})  
    return jsonify({"error": "Species not found"}), 404

@app.route('/api/routes/<int:species_id>', methods=['GET'])
def get_migration_routes(species_id):
    routes = MigrationRoute.query.filter_by(species_id=species_id).all()
    return jsonify([{'id': route.id, 
                     'start_lat': route.start_lat, 
                     'start_long': route.start_long,
                     'end_lat': route.end_lat, 
                     'end_long': route.end_long,
                     'time_of_year': route.time_of_year
                     } for route in routes])

