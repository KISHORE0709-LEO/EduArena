import { useRef, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Play, Pause, RotateCcw, Download } from "lucide-react";

interface VideoPlayerProps {
  videoUrl: string;
  isPlaying: boolean;
  onPlayPause: () => void;
  onRestart: () => void;
}

export const VideoPlayer = ({ videoUrl, isPlaying, onPlayPause, onRestart }: VideoPlayerProps) => {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    if (videoRef.current) {
      if (isPlaying) {
        videoRef.current.play();
      } else {
        videoRef.current.pause();
      }
    }
  }, [isPlaying]);

  const handleRestart = () => {
    if (videoRef.current) {
      videoRef.current.currentTime = 0;
      onRestart();
    }
  };

  const handleDownload = () => {
    const link = document.createElement('a');
    link.href = `http://localhost:8007${videoUrl}`;
    link.download = 'animation.mp4';
    link.click();
  };

  return (
    <div className="relative w-full h-[400px] bg-background/50 rounded-lg overflow-hidden">
      <video
        ref={videoRef}
        src={`http://localhost:8007${videoUrl}`}
        className="w-full h-full object-contain"
        controls={false}
        loop
      />
      
      <div className="absolute bottom-4 left-4 right-4 flex items-center gap-2">
        <Button
          size="sm"
          variant="secondary"
          onClick={onPlayPause}
          className="bg-background/80 backdrop-blur-sm"
        >
          {isPlaying ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
        </Button>
        
        <Button
          size="sm"
          variant="secondary"
          onClick={handleRestart}
          className="bg-background/80 backdrop-blur-sm"
        >
          <RotateCcw className="w-4 h-4" />
        </Button>
        
        <Button
          size="sm"
          variant="secondary"
          onClick={handleDownload}
          className="bg-background/80 backdrop-blur-sm ml-auto"
        >
          <Download className="w-4 h-4" />
        </Button>
      </div>
    </div>
  );
};