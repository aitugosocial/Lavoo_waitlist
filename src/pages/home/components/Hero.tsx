import { useState } from 'react';

export default function Hero() {
  const [email, setEmail] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState<'idle' | 'success' | 'error' | 'duplicate'>('idle');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || isSubmitting) return;

    setIsSubmitting(true);
    setSubmitStatus('idle');

    try {
      const formData = new URLSearchParams();
      formData.append('email', email);

      // Use the verified relative proxy path
      const response = await fetch('/api/waitlist', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData.toString(),
      });

      if (response.ok) {
        setSubmitStatus('success');
        setEmail('');
      } else if (response.status === 409) {
        // Handle explicit duplicate response from our backend
        setSubmitStatus('duplicate');
        setEmail('');
      } else {
        setSubmitStatus('error');
      }
    } catch (error) {
      setSubmitStatus('error');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <section className="relative min-h-screen flex items-center justify-center pt-20 pb-20 px-4 sm:px-6 lg:px-8 overflow-hidden">
      {/* Background gradient */}
      <div className="absolute inset-0 bg-gradient-to-br from-orange-50 via-white to-orange-50/30"></div>

      {/* Decorative elements */}
      <div className="absolute top-20 sm:top-40 right-10 sm:right-20 w-48 h-48 sm:w-96 sm:h-96 bg-orange-500/5 rounded-full blur-3xl"></div>
      <div className="absolute bottom-20 sm:bottom-40 left-10 sm:left-20 w-40 h-40 sm:w-80 sm:h-80 bg-orange-500/5 rounded-full blur-3xl"></div>

      <div className="relative max-w-6xl mx-auto w-full text-center">
        <div className="space-y-6 sm:space-y-8">
          <div className="inline-flex items-center px-4 py-2 bg-orange-500 text-white text-xs font-semibold rounded-full whitespace-nowrap">
            <i className="ri-rocket-line mr-2"></i>
            LAUNCHING SOON
          </div>

          <h1 className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl xl:text-8xl font-bold leading-tight px-4">
            <span className="text-gray-900 block mb-2">Insights That Drive</span>
            <span className="text-gray-900 block mb-2">Decisions</span>
            <span className="text-orange-500 block">Instantly.</span>
          </h1>

          <p className="text-lg sm:text-xl text-gray-600 leading-relaxed max-w-2xl mx-auto px-4">
            Your AI analyst delivers tailored, concise business intelligence, no complexity, just clarity.
          </p>

          {/* Hero Waitlist Form */}
          <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-4 max-w-xl mx-auto px-4" data-readdy-form id="hero-waitlist">
            <input
              type="email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your work email"
              required
              className="flex-1 px-6 py-4 text-base border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent"
            />
            <button
              type="submit"
              disabled={isSubmitting}
              className="px-8 py-4 bg-orange-500 text-white font-semibold rounded-lg hover:bg-orange-600 transition-all duration-300 flex items-center justify-center gap-2 whitespace-nowrap disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isSubmitting ? 'Joining...' : 'Join Waitlist'}
              <i className="ri-arrow-right-line"></i>
            </button>
          </form>

          {submitStatus === 'success' && (
            <p className="text-green-600 text-sm font-medium px-4">✓ You're on the list! We'll notify you at launch.</p>
          )}
          {submitStatus === 'duplicate' && (
            <p className="text-orange-600 text-sm font-medium px-4">✓ This email has already been waitlisted!</p>
          )}
          {submitStatus === 'error' && (
            <p className="text-red-600 text-sm font-medium px-4">Something went wrong. Please try again.</p>
          )}

          <p className="text-sm text-gray-500 px-4">
            Be the first to transform your data into action
          </p>
        </div>
      </div>
    </section>
  );
}