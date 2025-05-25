import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Welcome from './components/Welcome';
import Login from './components/auth/Login';
import RegisterUser from './components/auth/RegisterUser';
import RegisterDeveloper from './components/auth/RegisterDeveloper';
import RequireAuth from './components/auth/RequireAuth';

import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import DeveloperOnboarding from './pages/DeveloperOnboarding';
import NotFound from './pages/NotFound';

function App() {
  return (
    <Router>
      <Navbar />
      <div className="container">
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
            path="/onboarding"
            element={
              <RequireAuth>
                <DeveloperOnboarding />
              </RequireAuth>
            }
          />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
