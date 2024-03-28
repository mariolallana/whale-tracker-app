import React from 'react';
import whaleLogo from '../assets/whale.png'; // Ensure this path matches the location of your logo

const Header = () => {
  return (
    <header className="p-4 bg-whale-blue text-whale-white">
      <div className="container mx-auto flex items-center justify-between">
        <img src={whaleLogo} alt="Whale logo" className="h-12 w-12 mr-2" />
        <h1 className="text-4xl font-bold text-shadow-lg">Whale Tracking App</h1>
      </div>
    </header>
  );
};

export default Header;
