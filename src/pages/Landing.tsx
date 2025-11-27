import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { ArrowRight, Brain, Video, Zap, Sparkles } from "lucide-react";
import { Link } from "react-router-dom";
import Spline from '@splinetool/react-spline';
import Navbar from "@/components/Navbar";

const Landing = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-black text-white overflow-hidden">
      {/* Logo */}
      <div className="absolute top-6 left-6 z-20">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-full flex items-center justify-center">
            <Sparkles className="w-6 h-6 text-white" />
          </div>
          <span className="text-xl font-bold text-white">EduArena</span>
        </div>
      </div>

      {/* Background Effects */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-[600px] h-[600px] bg-cyan-500/15 rounded-full blur-3xl animate-pulse" />
        <div className="absolute -bottom-40 -left-40 w-[600px] h-[600px] bg-blue-500/15 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }} />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[700px] bg-yellow-500/10 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '2s' }} />
      </div>



      {/* Hero Section */}
      <main className="relative z-10 container mx-auto px-6 py-12">
        <div className="grid lg:grid-cols-2 gap-12 items-center min-h-[80vh]">
          {/* Left Side - 3D Robot */}
          <div className="relative h-[500px] lg:h-[600px]">
            <Spline scene="https://prod.spline.design/rU2-Ks0SC0T5od9B/scene.splinecode" />
          </div>

          {/* Right Side - Content */}
          <div className="space-y-8">
            <div className="space-y-6">
              <h1 className="text-5xl lg:text-6xl font-bold leading-tight">
                <span className="text-gray-300">Welcome to the</span>
                <br />
                <span className="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
                  Ultimate Edu Animation Arena
                </span>
              </h1>
              
              <p className="text-xl text-gray-400 leading-relaxed max-w-2xl">
                Type any math, physics, or CS concept and watch it become a fully animated educational video. 
                Auto-generated scenes, diagrams, and step-by-step visuals for students, teachers, and creators.
              </p>
            </div>

            {/* Feature Bullets */}
            <div className="space-y-4">
              {[
                "Text-to-Animation for Any Concept",
                "Auto-Generated Scenes and Diagrams", 
                "Instant Browser-Based Preview"
              ].map((feature, index) => (
                <div key={index} className="flex items-center gap-3">
                  <div className="w-2 h-2 bg-gradient-to-r from-yellow-400 to-cyan-400 rounded-full" />
                  <span className="text-gray-300">{feature}</span>
                </div>
              ))}
            </div>

            {/* CTA Buttons */}
            <div className="pt-4 flex flex-col sm:flex-row gap-4">
              <Link to="/signin">
                <Button size="lg" className="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-lg px-12 py-6 group shadow-lg shadow-cyan-500/25">
                  Enter the Arena
                  <ArrowRight className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
                </Button>
              </Link>
              <Button 
                size="lg" 
                variant="outline" 
                className="border-cyan-500/50 text-cyan-400 hover:bg-cyan-500/10 text-lg px-8 py-6"
                onClick={() => {
                  const video = document.createElement('video');
                  video.src = '/DEMO_VIDEO.mov';
                  video.controls = true;
                  video.autoplay = true;
                  video.style.cssText = 'position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);z-index:9999;max-width:90vw;max-height:90vh;border-radius:12px;box-shadow:0 25px 50px -12px rgba(0,0,0,0.8)';
                  const overlay = document.createElement('div');
                  overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.8);z-index:9998;display:flex;align-items:center;justify-content:center';
                  overlay.onclick = () => document.body.removeChild(overlay);
                  overlay.appendChild(video);
                  document.body.appendChild(overlay);
                }}
              >
                Watch Demo
              </Button>
            </div>

            {/* Stats */}
            <div className="grid grid-cols-3 gap-6 pt-8 border-t border-gray-800">
              {[
                { label: "Concepts Animated", value: "2.4K", accent: "text-yellow-400" },
                { label: "Scenes Generated", value: "12.8K", accent: "text-cyan-400" },
                { label: "Educators Onboard", value: "847", accent: "text-blue-400" }
              ].map((stat, index) => (
                <div key={index} className="text-center">
                  <div className={`text-2xl font-bold ${stat.accent}`}>{stat.value}</div>
                  <div className="text-sm text-gray-500">{stat.label}</div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Feature Strip */}
        <section className="py-20">
          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                icon: Brain,
                title: "Text Parsing to Scene Breakdown",
                description: "Advanced AI converts natural language into structured animation scenes and step-by-step visual instructions.",
                iconColor: "text-yellow-400"
              },
              {
                icon: Zap,
                title: "Smart Educational Visuals", 
                description: "Support for geometric shapes, graphs, vectors, algorithm animations, and complex scientific diagrams.",
                iconColor: "text-cyan-400"
              },
              {
                icon: Video,
                title: "One-Click Video Preview",
                description: "Instant rendering of playable animations with browser-based output and export capabilities.",
                iconColor: "text-blue-400"
              }
            ].map((feature, index) => (
              <Card key={index} className="bg-slate-900/50 border-slate-700/50 p-6 hover:border-cyan-500/40 transition-colors">
                <div className="space-y-4">
                  <div className="w-12 h-12 bg-slate-800/50 rounded-lg flex items-center justify-center">
                    <feature.icon className={`w-6 h-6 ${feature.iconColor}`} />
                  </div>
                  <h3 className="text-xl font-semibold text-white">{feature.title}</h3>
                  <p className="text-gray-400">{feature.description}</p>
                </div>
              </Card>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
};

export default Landing;