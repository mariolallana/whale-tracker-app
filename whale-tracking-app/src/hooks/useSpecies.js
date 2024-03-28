import { useEffect, useState } from 'react';

export const useSpecies = () => {
  const [species, setSpecies] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/species')
      .then(response => response.json())
      .then(data => setSpecies(data))
      .catch(error => console.error('Error fetching species:', error));
  }, []);

  return species;
};
