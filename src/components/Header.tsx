import { Code2, Github } from "lucide-react";
import { Button } from "@/components/ui/button";

export const Header = () => {
  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-gradient-primary rounded-lg flex items-center justify-center">
            <Code2 className="w-6 h-6 text-primary-foreground" />
          </div>
          <div>
            <h1 className="text-xl font-bold gradient-text">EduAnimate</h1>
            <p className="text-xs text-muted-foreground">Text to Animation</p>
          </div>
        </div>

        <nav className="flex items-center gap-4">
          <Button variant="ghost" size="sm" className="hidden md:flex">
            How it Works
          </Button>
          <Button variant="ghost" size="sm" className="hidden md:flex">
            Templates
          </Button>
          <Button variant="outline" size="sm">
            <Github className="w-4 h-4 mr-2" />
            GitHub
          </Button>
        </nav>
      </div>
    </header>
  );
};
