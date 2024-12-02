import React from 'react';
import { Link } from 'react-router-dom';

const App = () => {
  return (
    <div className="container mt-5 text-center">
      <h1 className="mb-4">Welcome to the JJ Diary</h1>
      <nav className="d-flex justify-content-center">
        <ul className="nav nav-pills">
          <li className="nav-item">
            <Link to="/login" className="nav-link">Login</Link>
          </li>
          <li className="nav-item">
            <Link to="/register" className="nav-link">Register</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default App;
