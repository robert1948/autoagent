import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Change if deploying
  headers: {
    'Content-Type': 'application/json',
  },
});

// Automatically add token to headers
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token'); // Or sessionStorage
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
