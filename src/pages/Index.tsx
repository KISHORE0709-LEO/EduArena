import { useState } from "react";
import Navbar from "@/components/Navbar";
import { HeroSection } from "@/components/HeroSection";
import { OutputPanel } from "@/components/OutputPanel";
import { AnimationGallery } from "@/components/AnimationGallery";
import { toast } from "sonner";

export interface Scene {
  id: number;
  duration: number;
  objects: any[];
  actions: any[];
}

export interface GenerateResponse {
  scenes: Scene[];
  stats: {
    scenesGenerated: number;
    timeMs: number;
  };
}

const Index = () => {
  const [isGenerating, setIsGenerating] = useState(false);
  const [inputText, setInputText] = useState("");
  const [generatedData, setGeneratedData] = useState<GenerateResponse | null>(null);

  const handleGenerate = async (description: string) => {
    setIsGenerating(true);
    setInputText(description);

    try {
      // Simulate processing delay
      await new Promise(resolve => setTimeout(resolve, 800));
      
      const { generateScenes } = await import("@/lib/sceneTemplates");
      const startTime = Date.now();
      const scenes = generateScenes(description);
      const timeMs = Date.now() - startTime;

      const data = {
        scenes,
        stats: {
          scenesGenerated: scenes.length,
          timeMs,
        },
      };
      
      setGeneratedData(data);
      toast.success("Animation generated successfully! ✨");
    } catch (error) {
      toast.error("Failed to generate animation");
      console.error(error);
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-black relative overflow-hidden">
      {/* Animated background elements */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute inset-0" style={{backgroundImage: 'radial-gradient(circle at 2px 2px, rgba(6,182,212,0.6) 2px, transparent 0)', backgroundSize: '40px 40px'}} />
        <div className="absolute -top-40 -right-40 w-[600px] h-[600px] bg-cyan-500/15 rounded-full blur-3xl animate-pulse" />
        <div className="absolute -bottom-40 -left-40 w-[600px] h-[600px] bg-blue-500/15 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }} />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[700px] bg-cyan-400/8 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '2s' }} />
        <div className="absolute top-20 right-20 w-[300px] h-[300px] bg-blue-400/10 rounded-full blur-2xl animate-pulse" style={{ animationDelay: '3s' }} />
        <div className="absolute bottom-20 left-20 w-[400px] h-[400px] bg-cyan-300/8 rounded-full blur-2xl animate-pulse" style={{ animationDelay: '4s' }} />
      </div>

      <div className="relative z-10">
        <Navbar />
        
        <HeroSection 
          onGenerate={handleGenerate} 
          isGenerating={isGenerating}
        />
        
        {generatedData ? (
          <div>
            <div className="text-center py-4">
              <button 
                onClick={() => setGeneratedData(null)}
                className="bg-slate-800/70 border-2 border-cyan-400/50 text-cyan-300 px-6 py-2 rounded-full hover:bg-slate-700/70 transition-all"
              >
                ← Back to Templates
              </button>
            </div>
            <OutputPanel 
              inputText={inputText}
              scenes={generatedData.scenes}
              stats={generatedData.stats}
            />
          </div>
        ) : (
          <AnimationGallery onSelect={handleGenerate} />
        )}
      </div>
    </div>
  );
};

export default Index;
