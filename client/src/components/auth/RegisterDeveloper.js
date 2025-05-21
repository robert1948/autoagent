import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function RegisterDeveloper() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    fullName: '',
    company: '',
    email: '',
    portfolio: '',
    password: '',
  });

  const [errors, setErrors] = useState({});
  const [submitting, setSubmitting] = useState(false);

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    setErrors({});

    try {
      const response = await axios.post('/api/register-developer', formData);
      if (response.data.success) {
        navigate('/onboarding'); // Next step: human review + API key
      } else {
        setErrors({ form: response.data.message || 'Something went wrong' });
      }
    } catch (err) {
      if (err.response && err.response.data) {
        setErrors(err.response.data.errors || { form: 'Registration failed' });
      } else {
        setErrors({ form: 'Server error' });
      }
    }

    setSubmitting(false);
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">Developer Registration</h2>
      {errors.form && <div className="alert alert-danger">{errors.form}</div>}

      <form onSubmit={handleSubmit} noValidate>
        <div className="mb-3">
          <label htmlFor="fullName" className="form-label">Full Name</label>
          <input
            type="text"
            className="form-control"
            id="fullName"
            name="fullName"
            value={formData.fullName}
            onChange={handleChange}
            required
          />
        </div>

        <div className="mb-3">
          <label htmlFor="company" className="form-label">Company / Organization</label>
          <input
            type="text"
            className="form-control"
            id="company"
            name="company"
            value={formData.company}
            onChange={handleChange}
            required
          />
        </div>

        <div className="mb-3">
          <label htmlFor="portfolio" className="form-label">GitHub / Portfolio URL</label>
          <input
            type="url"
            className="form-control"
            id="portfolio"
            name="portfolio"
            value={formData.portfolio}
            onChange={handleChange}
            required
          />
        </div>

        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email Address</label>
          <input
            type="email"
            className="form-control"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
          {errors.email && <small className="text-danger">{errors.email}</small>}
        </div>

        <div className="mb-3">
          <label htmlFor="password" className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>

        <button type="submit" className="btn btn-success" disabled={submitting}>
          {submitting ? 'Submitting...' : 'Apply as Developer'}
        </button>
      </form>
    </div>
  );
}

export default RegisterDeveloper;
