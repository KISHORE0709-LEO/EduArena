import type { APIRoute } from "@/types/api";
import { generateScenes } from "@/lib/sceneTemplates";

export const POST: APIRoute = async (request) => {
  try {
    const { description } = await request.json();

    if (!description || typeof description !== "string") {
      return new Response(
        JSON.stringify({ error: "Description is required" }),
        { status: 400, headers: { "Content-Type": "application/json" } }
      );
    }

    const startTime = Date.now();
    const scenes = generateScenes(description);
    const timeMs = Date.now() - startTime;

    return new Response(
      JSON.stringify({
        scenes,
        stats: {
          scenesGenerated: scenes.length,
          timeMs,
        },
      }),
      { status: 200, headers: { "Content-Type": "application/json" } }
    );
  } catch (error) {
    console.error("Scene generation error:", error);
    return new Response(
      JSON.stringify({ error: "Failed to generate scenes" }),
      { status: 500, headers: { "Content-Type": "application/json" } }
    );
  }
};
