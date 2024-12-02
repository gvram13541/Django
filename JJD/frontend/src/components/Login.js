import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('buyer');
  const [error, setError] = useState('');

  // Utility function to retrieve CSRF token from cookies
  const getCSRFToken = () => {
    const name = 'csrftoken';
    const cookies = document.cookie.split('; ');
    for (let cookie of cookies) {
      if (cookie.startsWith(name + '=')) {
        return cookie.split('=')[1];
      }
    }
    return null;
  };

  const handleLogin = async (e) => {
    e.preventDefault(); // Prevent default form submission
    try {
      // Get the CSRF token from cookies
      const csrftoken = getCSRFToken();
      console.log('CSRF Token:', csrftoken); // Debugging CSRF token

      // Make POST request with CSRF token included in headers
      const response = await axios.post(
        'http://localhost:8000/customers/login/',
        { email, password, role },
        {
          headers: {
            'X-CSRFToken': csrftoken,
          },
        }
      );

      localStorage.setItem('token', response.data.token);
      
      // Redirect to the appropriate home page based on role
      if (role === 'buyer') {
        window.location.href = '/buyer_home';
      } else {
        window.location.href = '/seller_home';
      }
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
    }
  };

  return (
    <div className="container mt-5">
      <h2>Login</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      <form onSubmit={handleLogin}>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email address</label>
          <input
            type="email"
            className="form-control"
            id="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="role" className="form-label">Role</label>
          <select
            className="form-select"
            id="role"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            required
          >
            <option value="buyer">Buyer</option>
            <option value="seller">Seller</option>
          </select>
        </div>
        <button type="submit" className="btn btn-primary">Login</button>
      </form>
    </div>
  );
};

export default Login;