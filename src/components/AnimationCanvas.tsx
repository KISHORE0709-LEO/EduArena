import { useEffect, useRef, useState } from "react";
import { Scene } from "@/pages/Index";

interface AnimationCanvasProps {
  scenes: Scene[];
  isPlaying: boolean;
}

export const AnimationCanvas = ({ scenes, isPlaying }: AnimationCanvasProps) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [currentScene, setCurrentScene] = useState(0);
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    if (!canvasRef.current || !isPlaying || scenes.length === 0) return;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animationFrame: number;
    let startTime = Date.now();
    const scene = scenes[currentScene];

    const animate = () => {
      const elapsed = Date.now() - startTime;
      const sceneProgress = Math.min(elapsed / scene.duration, 1);
      setProgress(sceneProgress);

      // Clear canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // Draw objects based on scene type
      renderScene(ctx, scene, sceneProgress, canvas.width, canvas.height);

      if (sceneProgress < 1) {
        animationFrame = requestAnimationFrame(animate);
      } else {
        // Move to next scene
        setTimeout(() => {
          setCurrentScene((prev) => (prev + 1) % scenes.length);
          setProgress(0);
          startTime = Date.now();
        }, 500);
      }
    };

    animationFrame = requestAnimationFrame(animate);

    return () => {
      if (animationFrame) cancelAnimationFrame(animationFrame);
    };
  }, [scenes, currentScene, isPlaying]);

  return (
    <div className="relative w-full h-[400px] bg-background/50 flex items-center justify-center">
      <canvas
        ref={canvasRef}
        width={600}
        height={400}
        className="max-w-full h-auto"
      />
      <div className="absolute bottom-4 left-4 right-4">
        <div className="flex items-center gap-2 text-xs text-muted-foreground">
          <span>Scene {currentScene + 1}/{scenes.length}</span>
          <div className="flex-1 h-1 bg-muted rounded-full overflow-hidden">
            <div
              className="h-full bg-primary transition-all duration-100"
              style={{ width: `${progress * 100}%` }}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

const renderScene = (
  ctx: CanvasRenderingContext2D,
  scene: Scene,
  progress: number,
  width: number,
  height: number
) => {
  const { objects, actions } = scene;

  // Set default styles
  ctx.font = "14px sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";

  objects.forEach((obj: any) => {
    const action = actions.find((a: any) => a.objectId === obj.id);
    
    // Calculate animated position/properties
    let x = obj.x;
    let y = obj.y;
    let scale = 1;
    let opacity = 1;

    if (action) {
      if (action.type === "move") {
        x = obj.x + (action.toX - obj.x) * easeInOutQuad(progress);
        y = obj.y + (action.toY - obj.y) * easeInOutQuad(progress);
      } else if (action.type === "scale") {
        scale = obj.scale + (action.toScale - obj.scale) * easeInOutQuad(progress);
      } else if (action.type === "fadeIn") {
        opacity = progress;
      } else if (action.type === "highlight") {
        opacity = 0.5 + Math.sin(progress * Math.PI * 4) * 0.5;
      }
    }

    ctx.globalAlpha = opacity;
    ctx.save();

    switch (obj.type) {
      case "rect":
        ctx.fillStyle = obj.color;
        ctx.fillRect(x - (obj.width * scale) / 2, y - (obj.height * scale) / 2, obj.width * scale, obj.height * scale);
        if (obj.label) {
          ctx.fillStyle = "#fff";
          ctx.fillText(obj.label, x, y);
        }
        break;

      case "circle":
        ctx.fillStyle = obj.color;
        ctx.beginPath();
        ctx.arc(x, y, obj.radius * scale, 0, Math.PI * 2);
        ctx.fill();
        if (obj.label) {
          ctx.fillStyle = "#fff";
          ctx.fillText(obj.label, x, y);
        }
        break;

      case "arrow":
        drawArrow(ctx, obj.startX, obj.startY, x, y, obj.color);
        if (obj.label) {
          ctx.fillStyle = obj.color;
          ctx.fillText(obj.label, (obj.startX + x) / 2, (obj.startY + y) / 2 - 15);
        }
        break;

      case "text":
        ctx.fillStyle = obj.color;
        ctx.font = `${obj.size}px sans-serif`;
        ctx.fillText(obj.label, x, y);
        break;

      case "line":
        ctx.strokeStyle = obj.color;
        ctx.lineWidth = obj.width || 2;
        ctx.beginPath();
        ctx.moveTo(obj.startX, obj.startY);
        ctx.lineTo(x, y);
        ctx.stroke();
        break;
    }

    ctx.restore();
    ctx.globalAlpha = 1;
  });
};

const drawArrow = (
  ctx: CanvasRenderingContext2D,
  fromX: number,
  fromY: number,
  toX: number,
  toY: number,
  color: string
) => {
  const headLength = 15;
  const angle = Math.atan2(toY - fromY, toX - fromX);

  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = 3;

  // Draw line
  ctx.beginPath();
  ctx.moveTo(fromX, fromY);
  ctx.lineTo(toX, toY);
  ctx.stroke();

  // Draw arrowhead
  ctx.beginPath();
  ctx.moveTo(toX, toY);
  ctx.lineTo(
    toX - headLength * Math.cos(angle - Math.PI / 6),
    toY - headLength * Math.sin(angle - Math.PI / 6)
  );
  ctx.lineTo(
    toX - headLength * Math.cos(angle + Math.PI / 6),
    toY - headLength * Math.sin(angle + Math.PI / 6)
  );
  ctx.closePath();
  ctx.fill();
};

const easeInOutQuad = (t: number): number => {
  return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
};
