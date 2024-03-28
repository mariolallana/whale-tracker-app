import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import SpeciesDropdown from './components/SpeciesDropdown';
import MapComponent from './components/MapComponent';
import SpeciesDetailsModal from './components/SpeciesDetailsModal'; // Corrected import statement
import useSpeciesDetails from './hooks/useSpeciesDetails';
import './App.css';


function App() {
  const [selectedSpeciesId, setSelectedSpeciesId] = useState(null);
  const [isModalVisible, setIsModalVisible] = useState(false);
  
  // Use the custom hook to fetch species details based on the selected species ID
  const { speciesDetails, isLoading } = useSpeciesDetails(selectedSpeciesId);

  // Automatically manage the visibility of the modal based on whether species details are available
  const handleCloseModal = () => setIsModalVisible(false);
  return (
    <div className="App">
      <Header />
      <main className="p-4">
        <SpeciesDropdown onSpeciesChange={(id) => {
          setSelectedSpeciesId(id);
          setIsModalVisible(!!id); // Show modal when a species is selected. Adjust as necessary.
        }} />
        <MapComponent selectedSpecies={selectedSpeciesId} />
        {!isLoading && speciesDetails && (
          <SpeciesDetailsModal
            species={speciesDetails}
            isVisible={isModalVisible}
            onClose={handleCloseModal}
          />
        )}
      </main>
      <Footer />
    </div>
  );
}

export default App;
