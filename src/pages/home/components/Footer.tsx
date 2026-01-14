export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-orange-500 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16">
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8 sm:gap-12 mb-12">
          {/* Left Column - Brand */}
          <div>
            <img 
              src="https://public.readdy.ai/ai/img_res/1ae07f77-6cb8-4b5d-879f-5b70288004bd.png" 
              alt="AI Analyst Engine" 
              className="h-10 w-auto mb-4 brightness-0 invert"
            />
            <p className="text-white/90 mb-6">
              Insights engineered for impact.
            </p>
            <div className="flex gap-4">
              <a 
                href="https://www.linkedin.com/search/results/all/?heroEntityKey=urn%3Ali%3Aorganization%3A106447017&keywords=AITugo&origin=ENTITY_SEARCH_HOME_HISTORY&sid=%40)H" 
                target="_blank" 
                rel="noopener noreferrer"
                className="w-10 h-10 bg-white/10 rounded-lg flex items-center justify-center hover:bg-white/20 transition-colors cursor-pointer"
              >
                <i className="ri-linkedin-fill text-xl"></i>
              </a>
              <a 
                href="https://twitter.com" 
                target="_blank" 
                rel="noopener noreferrer"
                className="w-10 h-10 bg-white/10 rounded-lg flex items-center justify-center hover:bg-white/20 transition-colors cursor-pointer"
              >
                <i className="ri-twitter-x-fill text-xl"></i>
              </a>
              <a 
                href="https://www.instagram.com/aitugo_?igsh=YzRtNjRjczFwdW51" 
                target="_blank" 
                rel="noopener noreferrer"
                className="w-10 h-10 bg-white/10 rounded-lg flex items-center justify-center hover:bg-white/20 transition-colors cursor-pointer"
              >
                <i className="ri-instagram-fill text-xl"></i>
              </a>
            </div>
          </div>

          {/* Middle Column - Product */}
          <div>
            <h4 className="text-sm font-bold uppercase tracking-wider mb-6">Product</h4>
            <ul className="space-y-3">
              <li>
                <a href="#features" className="text-white/90 hover:text-white transition-colors cursor-pointer">
                  Features
                </a>
              </li>
              <li>
                <a href="#benefits" className="text-white/90 hover:text-white transition-colors cursor-pointer">
                  Benefits
                </a>
              </li>
              <li>
                <a href="#waitlist" className="text-white/90 hover:text-white transition-colors cursor-pointer">
                  Pricing
                </a>
              </li>
              
            </ul>
          </div>

          {/* Right Column - Company */}
          <div>
            <h4 className="text-sm font-bold uppercase tracking-wider mb-6">Company</h4>
            <ul className="space-y-3">
              <li>
                <a href="#waitlist" className="text-white/90 hover:text-white transition-colors cursor-pointer">
                  About
                </a>
              </li>
              <li>
                <a href="#waitlist" className="text-white/90 hover:text-white transition-colors cursor-pointer">
                  Careers
                </a>
              </li>
              <li>
                <a href="#waitlist" className="text-white/90 hover:text-white transition-colors cursor-pointer">
                  Contact
                </a>
              </li>
              <li>
                <a href="#waitlist" className="text-white/90 hover:text-white transition-colors cursor-pointer">
                  Privacy
                </a>
              </li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-8 border-t border-white/20">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-white/90 text-sm text-center md:text-left">
              © {currentYear} GUUFS. All rights reserved.
            </p>
            <div className="flex flex-wrap justify-center gap-4 sm:gap-6">
              <a href="#waitlist" className="text-white/90 text-sm hover:text-white transition-colors cursor-pointer whitespace-nowrap">
                Terms of Service
              </a>
              <a href="#waitlist" className="text-white/90 text-sm hover:text-white transition-colors cursor-pointer whitespace-nowrap">
                Privacy Policy
              </a>
              <a 
                href="https://readdy.ai/?ref=logo" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-white/90 text-sm hover:text-white transition-colors cursor-pointer whitespace-nowrap"
              >
                Powered by GUUFS
              </a>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
