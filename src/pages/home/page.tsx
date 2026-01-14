import { useState, useEffect } from 'react';
import Hero from './components/Hero';
import Features from './components/Features';
import Benefits from './components/Benefits';
import WaitlistForm from './components/WaitlistForm';
import Footer from './components/Footer';

export default function HomePage() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <div className="min-h-screen bg-white">
      {/* Navigation */}
      <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 'bg-white shadow-md' : 'bg-transparent'}`}>
        <div className="max-w-7xl mx-auto px-8 py-4 flex items-center justify-between">
          <div className="flex items-center">
            <img 
              src="https://public.readdy.ai/ai/img_res/1ae07f77-6cb8-4b5d-879f-5b70288004bd.png" 
              alt="AI Analyst Engine Logo" 
              className="h-12 w-auto"
            />
          </div>
          <div className="flex items-center gap-8">
            <a href="#features" className={`text-sm font-medium transition-colors hover:text-orange-500 ${scrolled ? 'text-gray-700' : 'text-gray-800'}`}>
              Features
            </a>
            <a href="#benefits" className={`text-sm font-medium transition-colors hover:text-orange-500 ${scrolled ? 'text-gray-700' : 'text-gray-800'}`}>
              Benefits
            </a>
            <a href="#waitlist" className="text-sm font-medium text-orange-500 hover:text-orange-600 transition-colors">
              Join Waitlist
            </a>
          </div>
        </div>
      </nav>

      {/* Sections */}
      <Hero />
      <Features />
      <Benefits />
      <WaitlistForm />
      <Footer />
    </div>
  );
}
