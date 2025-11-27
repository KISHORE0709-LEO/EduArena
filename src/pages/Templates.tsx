import Navbar from "@/components/Navbar";

const Templates = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-black text-white relative overflow-hidden">
      <div className="absolute inset-0" style={{backgroundImage: 'radial-gradient(circle at 2px 2px, rgba(6,182,212,0.6) 2px, transparent 0)', backgroundSize: '40px 40px'}} />
      <div className="relative z-10">
        <Navbar />
        <div className="container mx-auto px-6 py-20">
          <h1 className="text-4xl font-bold text-center mb-8">Animation Templates</h1>
          <p className="text-gray-400 text-center max-w-2xl mx-auto mb-12">
            Browse our collection of pre-built templates for math, physics, and computer science concepts.
          </p>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {['Bubble Sort', 'Binary Tree', 'Vector Math', 'Pythagoras'].map((template, i) => (
              <div key={i} className="bg-slate-900/70 border-2 border-cyan-400/60 p-6 rounded-xl hover:scale-105 transition-transform cursor-pointer">
                <h3 className="text-lg font-bold text-cyan-400 mb-2">{template}</h3>
                <p className="text-gray-300 text-sm">Ready-to-use animation template</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Templates;