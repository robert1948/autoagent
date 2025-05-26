import { Link, useNavigate } from 'react-router-dom';
import { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { jwtDecode } from 'jwt-decode'; // ✅ Correct named import

const Navbar = () => {
  const navigate = useNavigate();
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const { token, user, isAuthenticated, logout } = useAuth();

  const toggleDropdown = () => setDropdownOpen(!dropdownOpen);

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  let displayName = 'User';
  if (token) {
    try {
      const decoded = jwtDecode(token);
      displayName = decoded.full_name || decoded.email || 'User';
    } catch {
      logout();
      navigate('/login');
    }
  }

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4">
      <Link className="navbar-brand" to="/">AutoAgent1</Link>

      <ul className="navbar-nav ms-auto">
        <li className="nav-item">
          <Link className="nav-link" to="/welcome">Welcome</Link>
        </li>

        {isAuthenticated ? (
          <>
            <li className="nav-item">
              <Link className="nav-link" to="/dashboard">Dashboard</Link>
            </li>
            <li className="nav-item dropdown">
              <button
                className="btn btn-link nav-link dropdown-toggle"
                onClick={toggleDropdown}
              >
                Hello, {displayName}
              </button>
              {dropdownOpen && (
                <ul className="dropdown-menu show">
                  <li><Link className="dropdown-item" to="/profile">Profile</Link></li>
                  <li><Link className="dropdown-item" to="/onboarding">Onboarding</Link></li>
                  <li><button className="dropdown-item" onClick={handleLogout}>Logout</button></li>
                </ul>
              )}
            </li>
          </>
        ) : (
          <>
            <li className="nav-item">
              <Link className="nav-link" to="/login">Login</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/register-user">Register</Link>
            </li>
          </>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
