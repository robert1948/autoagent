import { useState } from 'react';
import api from '../../api/axios';
import { useNavigate } from 'react-router-dom';

const RegisterDeveloper = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post('/register-developer', {
        email,
        password,
        full_name: fullName,
      });
      alert('Developer registered successfully!');
      navigate('/login');
    } catch (err) {
      alert('Developer registration failed: ' + (err.response?.data?.detail || 'Unknown error'));
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <h2>Register as Developer</h2>
      <input value={fullName} onChange={e => setFullName(e.target.value)} placeholder="Full Name" required />
      <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" required />
      <button type="submit">Register</button>
    </form>
  );
};

export default RegisterDeveloper;
