import { useState } from "react";
import { HeroSection } from "@/components/HeroSection";
import { OutputPanel } from "@/components/OutputPanel";
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
    <div className="min-h-screen bg-gradient-bg relative overflow-hidden">
      {/* Animated background elements */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-96 h-96 bg-primary/30 rounded-full blur-3xl animate-pulse" />
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-secondary/30 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }} />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-accent/20 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '2s' }} />
      </div>

      <div className="relative z-10">
        <HeroSection 
          onGenerate={handleGenerate} 
          isGenerating={isGenerating}
        />
        
        {generatedData && (
          <OutputPanel 
            inputText={inputText}
            scenes={generatedData.scenes}
            stats={generatedData.stats}
          />
        )}
      </div>
    </div>
  );
};

export default Index;
