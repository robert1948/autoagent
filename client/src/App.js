import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Suspense, lazy } from 'react';
import Navbar from './components/Navbar';
import RequireAuth from './components/auth/RequireAuth';

// Lazy loaded components
const Welcome = lazy(() => import('./components/Welcome'));
const Login = lazy(() => import('./components/auth/Login'));
const RegisterUser = lazy(() => import('./components/auth/RegisterUser'));
const RegisterDeveloper = lazy(() => import('./components/auth/RegisterDeveloper'));
const Home = lazy(() => import('./pages/Home'));
const Dashboard = lazy(() => import('./pages/Dashboard'));
const DeveloperOnboarding = lazy(() => import('./pages/DeveloperOnboarding')); // ✅ Keep only this one
const NotFound = lazy(() => import('./pages/NotFound'));

function App() {
  return (
    <Router>
      <div className="container">
        <Navbar />
        <Suspense fallback={<div>Loading...</div>}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/welcome" element={<Welcome />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register-user" element={<RegisterUser />} />
            <Route path="/register-developer" element={<RegisterDeveloper />} />
            <Route
              path="/dashboard"
              element={
                <RequireAuth>
                  <Dashboard />
                </RequireAuth>
              }
            />
            <Route
              path="/developer/onboarding"
              element={
                <RequireAuth>
                  <DeveloperOnboarding />
                </RequireAuth>
              }
            />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </Suspense>
      </div>
    </Router>
  );
}

export default App;
