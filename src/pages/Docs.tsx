import Navbar from "@/components/Navbar";

const Docs = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-black text-white relative overflow-hidden">
      <div className="absolute inset-0" style={{backgroundImage: 'radial-gradient(circle at 2px 2px, rgba(6,182,212,0.6) 2px, transparent 0)', backgroundSize: '40px 40px'}} />
      <div className="relative z-10">
        <Navbar />
        <div className="container mx-auto px-6 py-20">
          <h1 className="text-4xl font-bold text-center mb-8">Documentation</h1>
          <p className="text-gray-400 text-center max-w-2xl mx-auto mb-12">
            Complete guides, API references, and tutorials for getting started with EduArena.
          </p>
          <div className="grid md:grid-cols-2 gap-8">
            <div className="bg-slate-900/70 border-2 border-cyan-400/60 p-6 rounded-xl">
              <h3 className="text-xl font-bold text-cyan-400 mb-4">Getting Started</h3>
              <p className="text-gray-300">Learn the basics of creating your first animation with EduArena.</p>
            </div>
            <div className="bg-slate-900/70 border-2 border-cyan-400/60 p-6 rounded-xl">
              <h3 className="text-xl font-bold text-cyan-400 mb-4">API Reference</h3>
              <p className="text-gray-300">Complete API documentation for developers and integrations.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Docs;