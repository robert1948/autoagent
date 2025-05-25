import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { AuthProvider } from './context/AuthContext';

// ✅ Global styles
import 'bootstrap/dist/css/bootstrap.min.css';  // Bootstrap first
import './index.css';                           // Existing global styles
import './styles/master.css';                   // Your custom global overrides

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AuthProvider>
      <App />
    </AuthProvider>
  </React.StrictMode>
);
