import { useState } from 'react';

export default function WaitlistForm() {
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

      // Using relative path via Vite Proxy
      const relativePath = '/api/waitlist';
      const fullUrl = `${window.location.origin}${relativePath}`;
      console.log('DEBUG: Submitting to proxy URL:', fullUrl);

      const response = await fetch(relativePath, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: formData.toString(),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Success:', data);
        setSubmitStatus('success');
        setEmail('');
      } else if (response.status === 409) {
        // Email already exists in waitlist
        const errorData = await response.json();
        console.log('Duplicate email:', errorData);
        setSubmitStatus('duplicate');
        setEmail('');
      } else {
        // Other errors
        const errorData = await response.json();
        console.error('Error:', errorData);
        setSubmitStatus('error');
      }
    } catch (error) {
      console.error('Network error:', error);
      setSubmitStatus('error');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <section id="waitlist" className="py-24 bg-orange-500 relative overflow-hidden">
      {/* Decorative elements */}
      <div className="absolute top-0 left-0 w-96 h-96 bg-white/5 rounded-full blur-3xl"></div>
      <div className="absolute bottom-0 right-0 w-96 h-96 bg-white/5 rounded-full blur-3xl"></div>

      <div className="relative max-w-4xl mx-auto px-8 text-center">
        <h2 className="text-5xl lg:text-6xl font-bold text-white mb-6">
          Ready to see your data differently?
        </h2>
        <p className="text-xl text-white/90 mb-12">
          Join thousands on the waitlist. Launch access is limited.
        </p>

        {/* Waitlist Form */}
        <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-4 max-w-2xl mx-auto mb-6" data-readdy-form id="main-waitlist">
          <input
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your work email"
            required
            className="flex-1 px-6 py-5 text-base text-gray-900 bg-white rounded-lg focus:outline-none focus:ring-4 focus:ring-white/30"
          />
          <button
            type="submit"
            disabled={isSubmitting}
            className="px-10 py-5 bg-gray-900 text-white font-semibold rounded-lg hover:bg-gray-800 transition-all duration-300 flex items-center justify-center gap-2 whitespace-nowrap disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isSubmitting ? 'Securing...' : 'Secure Your Spot'}
            <i className="ri-arrow-right-line"></i>
          </button>
        </form>

        {submitStatus === 'success' && (
          <p className="text-white text-base font-medium mb-4">✓ Success! You're on the waitlist. Check your email for confirmation.</p>
        )}
        {submitStatus === 'duplicate' && (
          <p className="text-white text-base font-medium mb-4">✓ This email has already been waitlisted!</p>
        )}
        {submitStatus === 'error' && (
          <p className="text-white text-base font-medium mb-4">Something went wrong. Please try again.</p>
        )}


        <div className="mt-12">
          <p className="text-white/80 text-sm">
            No spam. Just launch updates and early access.
          </p>
        </div>
      </div>
    </section>
  );
}
