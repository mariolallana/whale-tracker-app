import React from 'react';

const SpeciesDetailsModal = ({ species, isVisible, onClose }) => {
  if (!isVisible || !species) return null;

  return (
    <div className="modal-backdrop fixed inset-0 bg-gray-600 bg-opacity-50">
    <div className="modal-content bg-whale-white rounded-lg shadow-xl max-w-lg mx-auto my-12 p-5">
      <button onClick={onClose} className="float-right bg-whale-blue text-whale-white rounded-full px-3 py-1">Close</button>
      <h2 className="text-2xl font-bold text-whale-blue mb-2">{species.name}</h2>
      <p className="text-md text-whale-grey">{species.description}</p>
      <p className="text-sm text-whale-grey mt-4">Conservation Status: {species.conservationStatus}</p>
      {/* Add more details as needed */}
    </div>
  </div>
  );
};

export default SpeciesDetailsModal;
