import Navbar from "@/components/Navbar";

const HowItWorks = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-black text-white relative overflow-hidden">
      <div className="absolute inset-0" style={{backgroundImage: 'radial-gradient(circle at 2px 2px, rgba(6,182,212,0.6) 2px, transparent 0)', backgroundSize: '40px 40px'}} />
      <div className="relative z-10">
        <Navbar />
        <div className="container mx-auto px-6 py-20">
          <h1 className="text-4xl font-bold text-center mb-8">How It Works</h1>
          <p className="text-gray-400 text-center max-w-2xl mx-auto mb-12">
            Learn the simple 3-step process to create educational animations from text descriptions.
          </p>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-slate-900/70 border-2 border-cyan-400/60 p-6 rounded-xl text-center">
              <div className="text-4xl mb-4">1️⃣</div>
              <h3 className="text-xl font-bold text-cyan-400 mb-4">Describe</h3>
              <p className="text-gray-300">Type any math, physics, or CS concept in natural language.</p>
            </div>
            <div className="bg-slate-900/70 border-2 border-cyan-400/60 p-6 rounded-xl text-center">
              <div className="text-4xl mb-4">2️⃣</div>
              <h3 className="text-xl font-bold text-cyan-400 mb-4">Generate</h3>
              <p className="text-gray-300">AI converts your text into structured animation scenes.</p>
            </div>
            <div className="bg-slate-900/70 border-2 border-cyan-400/60 p-6 rounded-xl text-center">
              <div className="text-4xl mb-4">3️⃣</div>
              <h3 className="text-xl font-bold text-cyan-400 mb-4">Watch</h3>
              <p className="text-gray-300">View your concept animated in real-time with smooth visuals.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HowItWorks;