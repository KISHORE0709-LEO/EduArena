import Navbar from "@/components/Navbar";

const Product = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-black text-white relative overflow-hidden">
      <div className="absolute inset-0" style={{backgroundImage: 'radial-gradient(circle at 2px 2px, rgba(6,182,212,0.6) 2px, transparent 0)', backgroundSize: '40px 40px'}} />
      <div className="relative z-10">
        <Navbar />
        <div className="container mx-auto px-6 py-20">
          <h1 className="text-4xl font-bold text-center mb-8">Product Features</h1>
          <p className="text-gray-400 text-center max-w-2xl mx-auto mb-12">
            Discover how EduArena transforms educational content creation with AI-powered animation generation.
          </p>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="bg-slate-900/70 border-2 border-cyan-400/60 p-6 rounded-xl">
              <h3 className="text-xl font-bold text-cyan-400 mb-4">AI-Powered Generation</h3>
              <p className="text-gray-300">Transform natural language into structured animation scenes automatically.</p>
            </div>
            <div className="bg-slate-900/70 border-2 border-cyan-400/60 p-6 rounded-xl">
              <h3 className="text-xl font-bold text-cyan-400 mb-4">Real-time Preview</h3>
              <p className="text-gray-300">See your animations come to life instantly with smooth 60fps rendering.</p>
            </div>
            <div className="bg-slate-900/70 border-2 border-cyan-400/60 p-6 rounded-xl">
              <h3 className="text-xl font-bold text-cyan-400 mb-4">Export Options</h3>
              <p className="text-gray-300">Download your animations as GIF, MP4, or interactive web components.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Product;