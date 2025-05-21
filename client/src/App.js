import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Auth Components
import RegisterUser from './components/auth/RegisterUser';
import RegisterDeveloper from './components/auth/RegisterDeveloper';
import Login from './components/auth/Login';
import EmailVerification from './components/auth/EmailVerification';

// Core Pages
import Home from './pages/Home'; // formerly LandingPage.js (rename accordingly)
import Welcome from './components/Welcome';
import Dashboard from './components/Dashboard';
import ErrorHandler from './components/ErrorHandler';
import DeveloperOnboarding from './pages/DeveloperOnboarding';
import NotFound from './pages/NotFound';

// Support
import HumanAgentWidget from './components/HumanAgentWidget';

function App() {
  return (
    <Router>
      <HumanAgentWidget /> {/* Optional global support widget */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/welcome" element={<Welcome />} />

        {/* Registration */}
        <Route path="/register-user" element={<RegisterUser />} />
        <Route path="/verify-email" element={<EmailVerification />} />
        <Route path="/register-developer" element={<RegisterDeveloper />} />
        <Route path="/onboarding" element={<DeveloperOnboarding />} />

        {/* Auth */}
        <Route path="/login" element={<Login />} />
        <Route path="/error" element={<ErrorHandler />} />

        {/* Dashboard */}
        <Route path="/dashboard" element={<Dashboard />} />

        {/* 404 Fallback */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
