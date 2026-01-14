export default function Features() {
  const features = [
    {
      icon: 'ri-line-chart-line',
      title: 'Real-Time Analysis',
      description: 'Live data processing delivers insights the moment they matter, not hours later.',
      color: 'bg-orange-500'
    },
    {
      icon: 'ri-focus-3-line',
      title: 'Tailored Outputs',
      description: 'Customized dashboards and reports that speak your industry\'s language, automatically.',
      color: 'bg-orange-500'
    },
    {
      icon: 'ri-bar-chart-box-line',
      title: 'Clear Visualizations',
      description: 'Complex data transformed into intuitive visuals that anyone on your team can understand.',
      color: 'bg-orange-500'
    }
  ];

  return (
    <section id="features" className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-8">
        {/* Section Header */}
        <div className="text-center mb-20">
          <div className="inline-block px-4 py-1 bg-orange-100 text-orange-600 text-xs font-bold uppercase tracking-wider rounded-full mb-6 whitespace-nowrap">
            CAPABILITIES
          </div>
          <h2 className="text-5xl lg:text-6xl font-bold mb-6">
            <span className="text-gray-900">Precision insights.</span>
            <br />
            <span className="text-orange-500">Zero complexity.</span>
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            Our AI engine analyzes, visualizes, and delivers, so you can act faster.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div
              key={index}
              className="bg-white p-8 rounded-2xl border border-gray-100 hover:shadow-xl transition-all duration-300 hover:-translate-y-2 group"
            >
              <div className={`w-14 h-14 ${feature.color} rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300`}>
                <i className={`${feature.icon} text-2xl text-white`}></i>
              </div>
              <h3 className="text-2xl font-bold text-gray-900 mb-4">
                {feature.title}
              </h3>
              <p className="text-gray-600 leading-relaxed">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
