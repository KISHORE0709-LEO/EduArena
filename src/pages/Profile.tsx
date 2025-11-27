import Navbar from "@/components/Navbar";

const Profile = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-black text-white relative overflow-hidden">
      <div className="absolute inset-0" style={{backgroundImage: 'radial-gradient(circle at 2px 2px, rgba(6,182,212,0.6) 2px, transparent 0)', backgroundSize: '40px 40px'}} />
      <div className="relative z-10">
        <Navbar />
        <div className="container mx-auto px-6 py-20">
          <h1 className="text-4xl font-bold text-center mb-8">Student Profile</h1>
          <div className="max-w-2xl mx-auto">
            <div className="bg-slate-900/70 border-2 border-cyan-400/60 p-8 rounded-xl">
              <div className="text-center mb-6">
                <div className="w-20 h-20 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-full mx-auto mb-4 flex items-center justify-center text-2xl font-bold">
                  JS
                </div>
                <h2 className="text-2xl font-bold text-cyan-400">John Student</h2>
                <p className="text-gray-400">Computer Science Student</p>
              </div>
              <div className="space-y-4">
                <div className="flex justify-between">
                  <span className="text-gray-300">Animations Created:</span>
                  <span className="text-cyan-400 font-bold">23</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-300">Concepts Learned:</span>
                  <span className="text-cyan-400 font-bold">15</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-300">Study Time:</span>
                  <span className="text-cyan-400 font-bold">12.5 hours</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;