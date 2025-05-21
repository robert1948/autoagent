import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../components/Navbar';

const LandingPage = () => {
  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-br from-white to-gray-100 text-gray-800">
      {/* Fixed Navbar */}
      <Navbar />

      {/* Hero Section */}
      <header className="pt-24 bg-white shadow px-4 text-center">
        <h1 className="text-5xl font-extrabold text-blue-700 tracking-tight">AutoAgent</h1>
        <p className="mt-4 text-xl text-gray-600">
          Your personal AI workforce. Automate anything. Anytime.
        </p>
        <div className="mt-6">
          <Link
            to="/register"
            className="inline-block px-6 py-3 bg-blue-600 text-white font-semibold rounded-full shadow hover:bg-blue-700 transition"
          >
            Get Started Free
          </Link>
        </div>
      </header>

      {/* Features Section */}
      <section className="py-20 px-6 max-w-6xl mx-auto">
        <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">
          Why Choose AutoAgent?
        </h2>
        <div className="grid md:grid-cols-3 gap-8">
          {[
            {
              title: 'Launch AI Agents',
              desc: 'Easily deploy agents like copywriters, schedulers, researchers and more.',
            },
            {
              title: 'Boost Your Output',
              desc: 'Let agents handle the repetitive work while you focus on growth.',
            },
            {
              title: 'Flexible & Affordable',
              desc: 'Pay-per-use or monthly plans. No contracts. Total freedom.',
            },
          ].map((feature, index) => (
            <div
              key={index}
              className="bg-white rounded-2xl shadow-lg p-8 text-center hover:shadow-xl transition"
            >
              <h3 className="text-xl font-semibold text-blue-700 mb-2">{feature.title}</h3>
              <p className="text-gray-600">{feature.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Call to Action Footer */}
      <footer className="mt-auto bg-white py-10 text-center border-t">
        <p className="text-gray-500 mb-4">Ready to automate your future?</p>
        <Link
          to="/register"
          className="inline-block px-6 py-2 text-white bg-blue-600 rounded-full font-medium hover:bg-blue-700 transition"
        >
          Create Your Account
        </Link>
        <p className="mt-6 text-sm text-gray-400">&copy; {new Date().getFullYear()} AutoAgent</p>
      </footer>
    </div>
  );
};

export default LandingPage;
