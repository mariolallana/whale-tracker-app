import React from 'react';

const Footer = () => {
  return (
    <footer className="text-center p-4 mt-8 bg-whale-blue text-whale-white">
      <p>Whale Tracking App © {new Date().getFullYear()}</p>
      {/* Add other footer content here */}
    </footer>
  );
};

export default Footer;
