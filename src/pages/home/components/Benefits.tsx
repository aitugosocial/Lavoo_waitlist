import { useState, useEffect } from 'react';

export default function Benefits() {
  const [currentSlide, setCurrentSlide] = useState(0);

  const benefits = [
    {
      label: 'EFFICIENCY',
      title: 'Hours saved.',
      titleAccent: 'Decisions accelerated.',
      description: 'Stop drowning in spreadsheets. Our engine surfaces what matters, filters what doesn\'t, and presents insights in seconds.',
      points: [
        'Automated data aggregation',
        'Instant report generation',
        'Smart anomaly detection'
      ]
    },
    {
      label: 'PRECISION',
      title: 'Accurate.',
      titleAccent: 'Actionable. Always.',
      description: 'AI-powered analysis that learns your business patterns, delivering reliable insights you can trust for critical decisions.',
      points: [
        'Machine learning accuracy',
        'Predictive analytics',
        'Contextual recommendations'
      ]
    },
    {
      label: 'SCALABILITY',
      title: 'Grows with you.',
      titleAccent: 'Adapts instantly.',
      description: 'From startup to enterprise, our platform scales seamlessly. Access insights anywhere, on any device, without compromise.',
      points: [
        'Multi-device compatibility',
        'Unlimited data processing',
        'Team collaboration tools'
      ]
    }
  ];

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % benefits.length);
    }, 10000);

    return () => clearInterval(timer);
  }, [benefits.length]);

  const goToSlide = (index: number) => {
    setCurrentSlide(index);
  };

  return (
    <section id="benefits" className="py-16 sm:py-20 lg:py-24 bg-gradient-to-b from-white to-orange-50/30 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        {/* Slideshow Container */}
        <div className="relative min-h-[500px] sm:min-h-[600px] flex items-center justify-center mb-16 sm:mb-20">
          {benefits.map((benefit, index) => (
            <div
              key={index}
              className={`absolute inset-0 transition-opacity duration-1000 ${
                currentSlide === index ? 'opacity-100' : 'opacity-0 pointer-events-none'
              }`}
            >
              <div className="max-w-3xl mx-auto text-center h-full flex flex-col justify-center">
                <div className="inline-block px-4 py-1 bg-orange-500 text-white text-xs font-bold uppercase tracking-wider rounded-full mb-6 whitespace-nowrap mx-auto">
                  {benefit.label}
                </div>
                <h3 className="text-3xl sm:text-4xl lg:text-5xl font-bold mb-6">
                  <span className="text-gray-900">{benefit.title}</span>
                  <br />
                  <span className="text-orange-500">{benefit.titleAccent}</span>
                </h3>
                <p className="text-base sm:text-lg text-gray-600 leading-relaxed mb-8">
                  {benefit.description}
                </p>
                <ul className="space-y-4 inline-block text-left mx-auto">
                  {benefit.points.map((point, idx) => (
                    <li key={idx} className="flex items-start gap-3">
                      <div className="w-6 h-6 bg-orange-500 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i className="ri-check-line text-white text-sm"></i>
                      </div>
                      <span className="text-gray-700 font-medium">{point}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          ))}

          {/* Slide Indicators */}
          <div className="absolute bottom-0 left-1/2 transform -translate-x-1/2 flex gap-3">
            {benefits.map((_, index) => (
              <button
                key={index}
                onClick={() => goToSlide(index)}
                className={`w-3 h-3 rounded-full transition-all duration-300 cursor-pointer ${
                  currentSlide === index ? 'bg-orange-500 w-8' : 'bg-gray-300 hover:bg-gray-400'
                }`}
                aria-label={`Go to slide ${index + 1}`}
              />
            ))}
          </div>
        </div>

        {/* Social Proof */}
        <div className="mt-20 sm:mt-24 lg:mt-32 bg-gray-50 rounded-3xl p-8 sm:p-12 lg:p-16">
          <h3 className="text-3xl sm:text-4xl font-bold text-center text-gray-900 mb-12 sm:mb-16">
            Trusted by forward-thinking teams
          </h3>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-8 sm:gap-12 mb-12 sm:mb-16">
            <div className="text-center">
              <div className="text-4xl sm:text-5xl lg:text-6xl font-bold text-orange-500 mb-2">10K+</div>
              <div className="text-gray-600 font-medium">Early adopters</div>
            </div>
            <div className="text-center">
              <div className="text-4xl sm:text-5xl lg:text-6xl font-bold text-orange-500 mb-2">94%</div>
              <div className="text-gray-600 font-medium">Satisfaction rate</div>
            </div>
            <div className="text-center">
              <div className="text-4xl sm:text-5xl lg:text-6xl font-bold text-orange-500 mb-2">2.5M+</div>
              <div className="text-gray-600 font-medium">Insights generated</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}