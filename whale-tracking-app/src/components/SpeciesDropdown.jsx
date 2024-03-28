import React from 'react';
import { useSpecies } from '../hooks/useSpecies';

const SpeciesDropdown = ({ onSpeciesChange }) => { // Ensure this prop is received
    const species = useSpecies();

    return (
        <div className="mb-4">
            <label htmlFor="species-select" className="block text-whale-grey font-medium text-sm mb-2">
                Select Cetacean Species
            </label>
            <select
                id="species-select"
                onChange={(e) => onSpeciesChange(e.target.value)} // Use the prop to handle selection changes
                className="block w-full py-2 px-4 bg-whale-white border border-whale-grey rounded-md shadow-lg text-gray-700 font-medium transition duration-150 ease-in-out focus:outline-none focus:ring-2 focus:ring-whale-blue focus:border-transparent"
            >
                <option value="">Select a species</option> {/* Add a default option */}
                {species.map((spec) => (
                    <option key={spec.id} value={spec.id}>{spec.name}</option>
                ))}
            </select>
        </div>
    );
};

export default SpeciesDropdown;
