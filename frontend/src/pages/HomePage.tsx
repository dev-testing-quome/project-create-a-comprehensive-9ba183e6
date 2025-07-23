import React from 'react';

const HomePage: React.FC = () => {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Welcome to the Citizen Services Portal</h1>
      <p className="text-lg mb-4">This portal provides access to various government services.</p>
      {/* Add links or sections for different services here */}
    </div>
  );
};

export default HomePage;