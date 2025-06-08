import { useState, useEffect } from "react";

const Navbar = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  // Close mobile menu when route changes (for regular HTML)
  // Remove this useEffect if not using React Router
  // useEffect(() => {
  //   setIsMobileMenuOpen(false);
  // }, [location]);

  // Close mobile menu on window resize (desktop)
  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth >= 768) {
        setIsMobileMenuOpen(false);
      }
    };

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  // Handle escape key to close menu
  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === "Escape" && isMobileMenuOpen) {
        setIsMobileMenuOpen(false);
      }
    };

    document.addEventListener("keydown", handleEscape);
    return () => document.removeEventListener("keydown", handleEscape);
  }, [isMobileMenuOpen]);

  // Prevent body scroll when mobile menu is open
  useEffect(() => {
    if (isMobileMenuOpen) {
      document.body.classList.add("mobile-menu-open");
    } else {
      document.body.classList.remove("mobile-menu-open");
    }

    // Cleanup on unmount
    return () => {
      document.body.classList.remove("mobile-menu-open");
    };
  }, [isMobileMenuOpen]);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  const closeMobileMenu = () => {
    setIsMobileMenuOpen(false);
  };

  // For regular HTML navigation without React Router
  const isActiveRoute = (path) => {
    return window.location.pathname === path;
  };

  const handleMobileMenuClick = (e) => {
    // Close menu if clicking the overlay (not the menu content)
    if (e.target === e.currentTarget) {
      closeMobileMenu();
    }
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        {/* Brand/Logo */}
        <a href="/" className="navbar-brand">
          AutoAgent
        </a>

        {/* Desktop Navigation */}
        <ul className="navbar-nav">
          <li className="nav-item">
            <a
              href="/"
              className={`nav-link ${isActiveRoute("/") ? "active" : ""}`}
            >
              Welcome
            </a>
          </li>
          <li className="nav-item">
            <a
              href="/login"
              className={`nav-link ${isActiveRoute("/login") ? "active" : ""}`}
            >
              Login
            </a>
          </li>
          <li className="nav-item">
            <a
              href="/register"
              className={`nav-link ${
                isActiveRoute("/register") ? "active" : ""
              }`}
            >
              Register
            </a>
          </li>
        </ul>

        {/* Hamburger Menu Button */}
        <button
          className={`hamburger-menu ${isMobileMenuOpen ? "active" : ""}`}
          onClick={toggleMobileMenu}
          aria-label="Toggle navigation"
          aria-expanded={isMobileMenuOpen}
        >
          <span className="hamburger-line"></span>
          <span className="hamburger-line"></span>
          <span className="hamburger-line"></span>
        </button>
      </div>

      {/* Mobile Menu Overlay */}
      <div
        className={`mobile-menu ${isMobileMenuOpen ? "active" : ""}`}
        onClick={handleMobileMenuClick}
      >
        <ul className="mobile-nav">
          <li className="mobile-nav-item">
            <a
              href="/"
              className={`mobile-nav-link ${
                isActiveRoute("/") ? "active" : ""
              }`}
              onClick={closeMobileMenu}
            >
              Welcome
            </a>
          </li>
          <li className="mobile-nav-item">
            <a
              href="/login"
              className={`mobile-nav-link ${
                isActiveRoute("/login") ? "active" : ""
              }`}
              onClick={closeMobileMenu}
            >
              Login
            </a>
          </li>
          <li className="mobile-nav-item">
            <a
              href="/register"
              className={`mobile-nav-link ${
                isActiveRoute("/register") ? "active" : ""
              }`}
              onClick={closeMobileMenu}
            >
              Register
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
