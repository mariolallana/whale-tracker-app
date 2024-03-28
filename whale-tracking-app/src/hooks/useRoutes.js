import { useEffect, useState } from 'react';

export const useRoutes = (selectedSpeciesId) => {
  const [routes, setRoutes] = useState([]);

  useEffect(() => {
    if (selectedSpeciesId) {
      fetch(`http://localhost:5000/api/routes/${selectedSpeciesId}`)
        .then(response => response.json())
        .then(data => setRoutes(data))
        .catch(error => console.error('Error fetching routes:', error));
    }
  }, [selectedSpeciesId]); // Re-run this effect if selectedSpeciesId changes

  return routes;
};
