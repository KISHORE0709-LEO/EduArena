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
  videoUrl?: string;
  status?: string;
}

const Index = () => {
  const [isGenerating, setIsGenerating] = useState(false);
  const [inputText, setInputText] = useState("");
  const [generatedData, setGeneratedData] = useState<GenerateResponse | null>(null);

  const handleGenerate = async (description: string) => {
    setIsGenerating(true);
    setInputText(description);

    try {
      const startTime = Date.now();
      
      // Start animation generation
      const response = await fetch('http://localhost:5000/generate-animation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ description: description }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const result = await response.json();
      const animationId = result.id;
      
      toast.info("Generating animation with Manim... This may take a moment.");
      
      if (result.success) {
        const timeMs = Date.now() - startTime;
        
        const data = {
          scenes: [],
          stats: {
            scenesGenerated: 1,
            timeMs,
          },
          videoUrl: result.video_url,
          instructions: result.instructions,
          status: 'completed'
        };
        
        setGeneratedData(data);
        toast.success("Animation Generated Successfully! 🎆");
      } else {
        toast.error(`Animation generation failed: ${result.error}`);
      }
      setIsGenerating(false);
      
    } catch (error) {
      toast.error("Failed to connect to animation service");
      console.error(error);
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
            
            {/* Show Complete Educational Video */}
            {generatedData.videoUrl && generatedData.status === 'completed' && generatedData.instructions ? (
              <div className="max-w-6xl mx-auto px-6 py-8">
                <div className="bg-slate-900/50 backdrop-blur-sm border border-cyan-400/20 rounded-2xl p-6">
                  <h2 className="text-3xl font-bold text-cyan-300 mb-6 text-center">Complete Educational Video</h2>
                  
                  {/* Main Content Grid */}
                  <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    
                    {/* Left Panel - Structured Instructions */}
                    <div className="lg:col-span-1">
                      {generatedData.instructions && (
                        <div className="bg-slate-800/50 rounded-lg border border-cyan-400/30 p-4 h-fit">
                          <h3 className="text-lg font-semibold text-cyan-200 mb-3 flex items-center">
                            📋 Structured Instructions
                          </h3>
                          
                          <div className="space-y-3">
                            <div className="bg-slate-700/30 p-3 rounded">
                              <div className="text-cyan-100 text-sm mb-1">
                                <strong>Concept:</strong>
                              </div>
                              <div className="text-white text-sm">{generatedData.instructions.concept}</div>
                            </div>
                            
                            {generatedData.instructions.description && (
                              <div className="bg-slate-700/30 p-3 rounded">
                                <div className="text-cyan-100 text-sm mb-1">
                                  <strong>Description:</strong>
                                </div>
                                <div className="text-white text-sm">{generatedData.instructions.description}</div>
                              </div>
                            )}
                            
                            {generatedData.instructions.scenes && (
                              <div className="bg-slate-700/30 p-3 rounded">
                                <div className="text-cyan-100 text-sm mb-2">
                                  <strong>Animation Scenes:</strong>
                                </div>
                                <div className="space-y-2">
                                  {generatedData.instructions.scenes.map((scene, index) => (
                                    <div key={index} className="text-xs text-cyan-300 bg-slate-600/40 p-2 rounded">
                                      <div className="font-medium">Scene {scene.id}: {scene.title}</div>
                                      <div className="text-cyan-400">Duration: {scene.duration}s</div>
                                      {scene.action && <div className="text-gray-300">Action: {scene.action}</div>}
                                    </div>
                                  ))}
                                </div>
                              </div>
                            )}
                            
                            {generatedData.instructions.educational_points && (
                              <div className="bg-slate-700/30 p-3 rounded">
                                <div className="text-cyan-100 text-sm mb-2">
                                  <strong>Learning Points:</strong>
                                </div>
                                <ul className="space-y-1">
                                  {generatedData.instructions.educational_points.map((point, index) => (
                                    <li key={index} className="text-xs text-white flex items-start">
                                      <span className="text-cyan-400 mr-2">•</span>
                                      {point}
                                    </li>
                                  ))}
                                </ul>
                              </div>
                            )}
                          </div>
                        </div>
                      )}
                    </div>
                    
                    {/* Center Panel - Main Video */}
                    <div className="lg:col-span-2">
                  
                      {/* Main Video Player */}
                      <div className="bg-slate-800/30 rounded-lg border border-cyan-400/30 p-4 mb-4">
                        <h4 className="text-lg font-semibold text-cyan-200 mb-3 flex items-center">
                          🎬 Main Educational Video
                        </h4>
                        <div className="flex justify-center">
                          <video 
                            controls 
                            preload="metadata"
                            className="max-w-full h-auto rounded-lg border border-cyan-400/30 shadow-2xl"
                            src={`http://localhost:5000${generatedData.videoUrl}`}
                            onLoadedMetadata={(e) => {
                              console.log('Video duration:', e.target.duration);
                            }}
                          >
                            Your browser does not support the video tag.
                          </video>
                        </div>
                        <div className="mt-2 text-center text-sm text-cyan-300">
                          Full duration video with complete educational content
                        </div>
                      </div>
                  
                      {/* Additional Videos */}
                      {(generatedData.animation_url || generatedData.explanation_url) && (
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                          {generatedData.animation_url && (
                            <div className="bg-slate-800/30 p-4 rounded-lg border border-cyan-400/20">
                              <h4 className="text-md font-semibold text-cyan-200 mb-2 flex items-center">
                                🎬 Visual Animation Only
                              </h4>
                              <video 
                                controls 
                                preload="metadata"
                                className="w-full h-auto rounded border border-cyan-400/20"
                                src={`http://localhost:5000${generatedData.animation_url}`}
                                onLoadedMetadata={(e) => {
                                  console.log('Animation duration:', e.target.duration);
                                }}
                              />
                              <div className="mt-1 text-xs text-cyan-400">Pure visual demonstration</div>
                            </div>
                          )}
                          {generatedData.explanation_url && (
                            <div className="bg-slate-800/30 p-4 rounded-lg border border-cyan-400/20">
                              <h4 className="text-md font-semibold text-cyan-200 mb-2 flex items-center">
                                📚 Educational Explanation Only
                              </h4>
                              <video 
                                controls 
                                preload="metadata"
                                className="w-full h-auto rounded border border-cyan-400/20"
                                src={`http://localhost:5000${generatedData.explanation_url}`}
                                onLoadedMetadata={(e) => {
                                  console.log('Explanation duration:', e.target.duration);
                                }}
                              />
                              <div className="mt-1 text-xs text-cyan-400">Concept explanation and learning points</div>
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  </div>
                  
                  {/* Summary Section */}
                  <div className="mt-6 bg-slate-800/50 rounded-lg border border-cyan-400/30 p-4">
                    <h3 className="text-xl font-semibold text-cyan-200 mb-3 flex items-center">
                      🎯 Complete Educational Package
                    </h3>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-center">
                      <div className="bg-slate-700/30 p-3 rounded">
                        <div className="text-2xl mb-2">📋</div>
                        <div className="text-cyan-200 font-medium">Structured Instructions</div>
                        <div className="text-xs text-cyan-400 mt-1">JSON format with scenes & duration</div>
                      </div>
                      <div className="bg-slate-700/30 p-3 rounded">
                        <div className="text-2xl mb-2">🎬</div>
                        <div className="text-cyan-200 font-medium">Visual Animation</div>
                        <div className="text-xs text-cyan-400 mt-1">Professional Manim rendering</div>
                      </div>
                      <div className="bg-slate-700/30 p-3 rounded">
                        <div className="text-2xl mb-2">📚</div>
                        <div className="text-cyan-200 font-medium">Educational Explanation</div>
                        <div className="text-xs text-cyan-400 mt-1">Concept breakdown & learning points</div>
                      </div>
                    </div>
                  </div>
                  
                  <div className="text-center">
                    <p className="text-cyan-200 mb-2">Input: "{inputText}"</p>
                    <p className="text-sm text-cyan-400/70 mb-4">Complete Educational Video with Instructions + Animation + Explanation</p>
                    <div className="flex flex-wrap justify-center gap-3">
                      <a 
                        href={`http://localhost:5000${generatedData.videoUrl}`}
                        download="complete_educational_video.mp4"
                        className="inline-flex items-center gap-2 bg-cyan-600 hover:bg-cyan-700 text-white px-4 py-2 rounded-lg transition-colors"
                      >
                        📥 Download Complete Video
                      </a>
                      {generatedData.animation_url && (
                        <a 
                          href={`http://localhost:5000${generatedData.animation_url}`}
                          download="animation_only.mp4"
                          className="inline-flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors"
                        >
                          🎬 Download Animation
                        </a>
                      )}
                      {generatedData.explanation_url && (
                        <a 
                          href={`http://localhost:5000${generatedData.explanation_url}`}
                          download="explanation_only.mp4"
                          className="inline-flex items-center gap-2 bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-lg transition-colors"
                        >
                          📚 Download Explanation
                        </a>
                      )}
                    </div>
                  </div>
                </div>
              </div>
            ) : (
              <OutputPanel 
                inputText={inputText}
                scenes={generatedData.scenes}
                stats={generatedData.stats}
              />
            )}
          </div>
        ) : (
          <AnimationGallery onSelect={handleGenerate} />
        )}
      </div>
    </div>
  );
};

export default Index;
