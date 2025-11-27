import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Slider } from "@/components/ui/slider";
import { Play, Pause, RotateCcw, Code2, Sparkles, Download, Gauge } from "lucide-react";
import { AnimationCanvas } from "@/components/AnimationCanvas";
import { Scene } from "@/pages/Index";
import { toast } from "sonner";

interface OutputPanelProps {
  inputText: string;
  scenes: Scene[];
  stats: {
    scenesGenerated: number;
    timeMs: number;
  };
}

export const OutputPanel = ({ inputText, scenes, stats }: OutputPanelProps) => {
  const [isPlaying, setIsPlaying] = useState(true);
  const [showJson, setShowJson] = useState(false);
  const [playbackSpeed, setPlaybackSpeed] = useState(1);

  const handleExport = () => {
    toast.success("Export feature coming soon! 🎬");
  };

  return (
    <section className="container mx-auto px-4 pb-16">
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Stats Banner */}
        <div className="glass-panel p-4 flex items-center justify-center gap-8 text-sm animate-fade-in">
          <div className="flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-accent" />
            <span className="text-muted-foreground">
              <span className="font-bold text-foreground">{stats.scenesGenerated}</span> scenes generated
            </span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 bg-primary rounded-full animate-pulse" />
            <span className="text-muted-foreground">
              in <span className="font-bold text-foreground">{stats.timeMs}ms</span>
            </span>
          </div>
        </div>

        {/* Split Panel */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Left: Text & JSON */}
          <Card className="glass-panel p-6 space-y-4 animate-fade-in">
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold flex items-center gap-2">
                <Code2 className="w-5 h-5 text-primary" />
                {showJson ? "Scene Instructions" : "Input Text"}
              </h3>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setShowJson(!showJson)}
                className="border-primary/50 hover:bg-primary/10"
              >
                {showJson ? "Show Input" : "Show JSON"}
              </Button>
            </div>

            <div className="bg-muted/30 rounded-lg p-4 h-[400px] overflow-auto">
              {showJson ? (
                <pre className="text-xs text-foreground/80 font-mono">
                  {JSON.stringify(scenes, null, 2)}
                </pre>
              ) : (
                <p className="text-muted-foreground whitespace-pre-wrap">{inputText}</p>
              )}
            </div>
          </Card>

          {/* Right: Animation Canvas */}
          <Card className="glass-panel p-6 space-y-4 animate-fade-in delay-100">
            <div className="flex items-center justify-between">
              <h3 className="text-lg font-semibold flex items-center gap-2">
                <Play className="w-5 h-5 text-accent" />
                Animation Output
              </h3>
              <div className="flex gap-2">
                <Button
                  variant="outline"
                  size="icon"
                  onClick={() => setIsPlaying(!isPlaying)}
                  className="border-accent/50 hover:bg-accent/10"
                >
                  {isPlaying ? (
                    <Pause className="w-4 h-4" />
                  ) : (
                    <Play className="w-4 h-4" />
                  )}
                </Button>
                <Button
                  variant="outline"
                  size="icon"
                  onClick={() => {
                    setIsPlaying(false);
                    setTimeout(() => setIsPlaying(true), 100);
                  }}
                  className="border-secondary/50 hover:bg-secondary/10"
                >
                  <RotateCcw className="w-4 h-4" />
                </Button>
                <Button
                  variant="outline"
                  size="icon"
                  onClick={handleExport}
                  className="border-primary/50 hover:bg-primary/10"
                >
                  <Download className="w-4 h-4" />
                </Button>
              </div>
            </div>

            <div className="bg-muted/30 rounded-lg overflow-hidden">
              <AnimationCanvas scenes={scenes} isPlaying={isPlaying} speed={playbackSpeed} />
            </div>

            {/* Speed Control */}
            <div className="space-y-2">
              <div className="flex items-center justify-between text-sm">
                <span className="flex items-center gap-2 text-muted-foreground">
                  <Gauge className="w-4 h-4" />
                  Speed: {playbackSpeed}x
                </span>
              </div>
              <Slider
                value={[playbackSpeed]}
                onValueChange={(value) => setPlaybackSpeed(value[0])}
                min={0.25}
                max={2}
                step={0.25}
                className="w-full"
              />
            </div>
          </Card>
        </div>

        {/* Before/After Comparison */}
        <div className="glass-panel p-8 text-center space-y-4 animate-fade-in delay-200">
          <div className="flex items-center justify-center gap-4 text-muted-foreground">
            <div className="flex-1 text-right">
              <div className="font-semibold text-foreground">Before</div>
              <div className="text-sm">Raw text input</div>
            </div>
            <div className="w-12 h-12 bg-gradient-primary rounded-full flex items-center justify-center">
              <Sparkles className="w-6 h-6 text-primary-foreground" />
            </div>
            <div className="flex-1 text-left">
              <div className="font-semibold text-foreground">After</div>
              <div className="text-sm">Structured animation</div>
            </div>
          </div>
          <p className="text-sm text-muted-foreground max-w-2xl mx-auto">
            Watch how natural language transforms into precise scene instructions and renders as smooth animations
          </p>
        </div>
      </div>
    </section>
  );
};
