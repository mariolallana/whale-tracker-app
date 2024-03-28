import React from 'react';
import { MapContainer, TileLayer, Polyline, Marker, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { useRoutes } from '../hooks/useRoutes'; // Assumes this hook fetches the routes
import L from 'leaflet';
import whaleIconPath from '../assets/whale.png'; // Ensure this path is correct

const AutoAdjustMap = ({ routePositions }) => {
  const map = useMap();

  React.useEffect(() => {
    if (routePositions && routePositions.length > 0) {
      const bounds = L.latLngBounds(routePositions);
      map.fitBounds(bounds);
    }
  }, [routePositions, map]);

  return null;
};

const MapComponent = ({ selectedSpecies }) => {
  const routes = useRoutes(selectedSpecies);
  const whaleIcon = new L.Icon({
    iconUrl: whaleIconPath,
    iconSize: [32, 32],
    iconAnchor: [16, 16],
  });

  // Calculate the entire migration path
  const migrationPath = routes.map(route => [
    [route.start_lat, route.start_long],
    [route.end_lat, route.end_long]
  ]).flat(); // Flatten the array since each route has two points

  // Current month and whale position for the icon
  const currentMonth = new Date().getMonth() + 1;
  console.log('Current month type:', typeof currentMonth); // Should log "number"

  //const currentRoute = routes.find(route => route.time_of_year === currentMonth);
  //const whalePosition = currentRoute ? [currentRoute.start_lat, currentRoute.start_long] : null;

  // After fetching routes, log the type of time_of_year for the first route as an example
  if(routes.length > 0){
      console.log('time_of_year type for first route:', typeof routes[0].time_of_year);
  }

  // Find the route for the current month
  let whalePosition = null;
  routes.forEach(route => {
    console.log(`Checking route: `, route);
    if(route.time_of_year === currentMonth){
      // Set whale position to the start of this month's route
      whalePosition = [route.start_lat, route.start_long];
      console.log(`Whale position for month ${currentMonth}:`, whalePosition);
    }
  });

  // Ensure there's logic to handle the case where no route matches the current month
  if (!whalePosition) {
    console.log(`No matching route found for the current month. ${currentMonth}`);
    // You might want to handle this case explicitly, e.g., by showing the whale in a default position or not at all
  }

  return (
    <div className="rounded-lg overflow-hidden shadow-lg my-5 mx-auto max-w-3xl">
      <MapContainer center={[20, 0]} zoom={2} style={{ height: '400px', width: '100%' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        <Polyline positions={migrationPath} color="blue" weight={4} />
        {whalePosition && <Marker position={whalePosition} icon={whaleIcon} />}
        <AutoAdjustMap routePositions={migrationPath} />
      </MapContainer>
    </div>
  );
};

export default MapComponent;
