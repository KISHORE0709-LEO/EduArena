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
  "merge sort algorithm",
  "quick sort visualization",
  "linked list insert node",
  "stack push and pop",
  "breadth first search",
  "vector addition",
  "Pythagoras theorem",
  "binary search tree insert",
  "matrix 2x2 multiply",
  "derivative visualization",
  "factorial animation",
];

export const HeroSection = ({ onGenerate, isGenerating }: HeroSectionProps) => {
  const [description, setDescription] = useState("");

  const handleSubmit = () => {
    if (description.trim()) {
      onGenerate(description);
      setTimeout(() => {
        const outputSection = document.querySelector('[data-output-section]');
        if (outputSection) {
          outputSection.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100);
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
            <Lightbulb className="w-6 h-6 text-cyan-400 mt-1 flex-shrink-0" />
            <Select onValueChange={handleExampleSelect}>
              <SelectTrigger className="w-full md:w-64 bg-slate-800/70 border-2 border-cyan-400/50 focus:border-cyan-300 shadow-lg shadow-cyan-400/25">
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
            className="min-h-[200px] text-lg bg-slate-800/50 border-2 border-cyan-400/50 focus:border-cyan-300 resize-none shadow-lg shadow-cyan-400/25 focus:shadow-cyan-300/35"
          />

          <Button
            size="lg"
            onClick={handleSubmit}
            disabled={isGenerating || !description.trim()}
            className="w-full md:w-auto px-12 py-6 text-lg font-semibold bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 transition-all shadow-lg shadow-cyan-500/25 hover:shadow-cyan-500/40"
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


      </div>
    </section>
  );
};
