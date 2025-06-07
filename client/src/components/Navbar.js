// client/src/components/Navbar.js

import React, { useState } from "react";
import '../styles/_navbar.scss'; // ✅ Correct relative path

const Navbar = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => setMenuOpen(!menuOpen);

  return (
    <nav className="navbar">
      <div className="navbar-brand">AutoAgent</div>
      <div className="navbar-toggle" onClick={toggleMenu}>
        &#9776; {/* Unicode hamburger icon */}
      </div>
      <div className={`navbar-menu ${menuOpen ? "active" : ""}`}>
        <a href="/welcome">Welcome</a>
        <a href="/login">Login</a>
        <a href="/register">Register</a>
      </div>
    </nav>
  );
};

export default Navbar;
