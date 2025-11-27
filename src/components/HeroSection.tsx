import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Sparkles, Lightbulb } from "lucide-react";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

interface HeroSectionProps {
  onGenerate: (description: string) => void;
  isGenerating: boolean;
}

const EXAMPLE_PROMPTS = [
  "bubble sort 6 numbers",
  "vector addition",
  "Pythagoras theorem",
  "binary search tree insert [1,5,3]",
  "matrix 2x2 multiply",
];

export const HeroSection = ({ onGenerate, isGenerating }: HeroSectionProps) => {
  const [description, setDescription] = useState("");

  const handleSubmit = () => {
    if (description.trim()) {
      onGenerate(description);
    }
  };

  const handleExampleSelect = (value: string) => {
    setDescription(value);
  };

  return (
    <section className="container mx-auto px-4 py-16 md:py-24">
      <div className="max-w-4xl mx-auto text-center space-y-8">
        {/* Header */}
        <div className="space-y-4 animate-fade-in">
          <h1 className="text-5xl md:text-7xl font-bold gradient-text leading-tight">
            Text-to-Edu Animation
          </h1>
          
          <p className="text-xl md:text-2xl text-muted-foreground max-w-2xl mx-auto">
            Transform any math or CS concept into beautiful, interactive animations instantly
          </p>
        </div>

        {/* Input Area */}
        <div className="glass-panel p-8 space-y-6 animate-scale-in">
          <div className="flex items-start gap-4">
            <Lightbulb className="w-6 h-6 text-accent mt-1 flex-shrink-0" />
            <Select onValueChange={handleExampleSelect}>
              <SelectTrigger className="w-full md:w-64 bg-muted/50 border-border">
                <SelectValue placeholder="Try an example..." />
              </SelectTrigger>
              <SelectContent>
                {EXAMPLE_PROMPTS.map((prompt) => (
                  <SelectItem key={prompt} value={prompt}>
                    {prompt}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>

          <Textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Describe any math or CS concept here...&#10;&#10;Examples:&#10;• Show bubble sort on [4,2,7,1,3]&#10;• Explain vector addition with two arrows&#10;• Demonstrate Pythagoras theorem visually"
            className="min-h-[200px] text-lg bg-muted/30 border-border focus:border-primary resize-none"
          />

          <Button
            size="lg"
            onClick={handleSubmit}
            disabled={isGenerating || !description.trim()}
            className="w-full md:w-auto px-12 py-6 text-lg font-semibold bg-gradient-primary hover:opacity-90 transition-all animate-glow"
          >
            {isGenerating ? (
              <>
                <div className="w-5 h-5 border-2 border-primary-foreground/30 border-t-primary-foreground rounded-full animate-spin mr-2" />
                Generating Animation...
              </>
            ) : (
              <>
                <Sparkles className="w-5 h-5 mr-2" />
                Generate Animation
              </>
            )}
          </Button>
        </div>

        {/* Features */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-8">
          {[
            { icon: "⚡", title: "Instant Generation", desc: "Scene JSON in ~800ms" },
            { icon: "🎨", title: "5+ Templates", desc: "Sort, vectors, graphs & more" },
            { icon: "📹", title: "Smooth Playback", desc: "Canvas-based animation" },
          ].map((feature, i) => (
            <div
              key={i}
              className="glass-panel p-6 text-center space-y-2 hover:scale-105 transition-transform"
            >
              <div className="text-4xl">{feature.icon}</div>
              <h3 className="font-semibold text-foreground">{feature.title}</h3>
              <p className="text-sm text-muted-foreground">{feature.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
