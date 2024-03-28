import { useState, useEffect } from 'react';

const useSpeciesDetails = (selectedSpeciesId) => {
  const [speciesDetails, setSpeciesDetails] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    if (selectedSpeciesId) {
      setIsLoading(true);
      fetch(`http://localhost:5000/api/species/${selectedSpeciesId}`)
        .then((response) => response.json())
        .then((data) => {
          setSpeciesDetails(data);
          setIsLoading(false);
        })
        .catch((error) => {
          console.error('Error fetching species details:', error);
          setIsLoading(false);
        });
    } else {
      setSpeciesDetails(null); // Reset when no species is selected
    }
  }, [selectedSpeciesId]);

  return { speciesDetails, isLoading };
};

export default useSpeciesDetails;
