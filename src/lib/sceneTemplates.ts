import { Scene } from "@/pages/Index";

export const generateScenes = (description: string): Scene[] => {
  const lowerDesc = description.toLowerCase();

  if (lowerDesc.includes("sort") || lowerDesc.includes("bubble")) {
    return bubbleSortScenes();
  } else if (lowerDesc.includes("vector")) {
    return vectorAdditionScenes();
  } else if (lowerDesc.includes("pythagoras") || lowerDesc.includes("theorem")) {
    return pythagorasScenes();
  } else if (lowerDesc.includes("tree") || lowerDesc.includes("bst")) {
    return binaryTreeScenes();
  } else if (lowerDesc.includes("matrix")) {
    return matrixMultiplyScenes();
  }

  return defaultGraphScenes();
};

const bubbleSortScenes = (): Scene[] => {
  const values = [4, 2, 7, 1, 5, 3];
  const barWidth = 60;
  const spacing = 20;
  const startX = 150;
  const baseY = 300;

  return [
    // Initial state
    {
      id: 0,
      duration: 1500,
      objects: values.map((val, i) => ({
        id: i,
        type: "rect",
        x: startX + i * (barWidth + spacing),
        y: baseY - val * 15,
        width: barWidth,
        height: val * 30,
        color: "#22d3ee",
        label: val.toString(),
        scale: 1,
      })),
      actions: values.map((_, i) => ({
        objectId: i,
        type: "fadeIn",
      })),
    },
    // Compare 4 and 2 (swap needed)
    {
      id: 1,
      duration: 2000,
      objects: [
        ...values.slice(0, 2).map((val, i) => ({
          id: i,
          type: "rect",
          x: startX + i * (barWidth + spacing),
          y: baseY - val * 15,
          width: barWidth,
          height: val * 30,
          color: i === 0 ? "#f97316" : "#22d3ee",
          label: val.toString(),
          scale: 1,
        })),
        ...values.slice(2).map((val, i) => ({
          id: i + 2,
          type: "rect",
          x: startX + (i + 2) * (barWidth + spacing),
          y: baseY - val * 15,
          width: barWidth,
          height: val * 30,
          color: "#22d3ee",
          label: val.toString(),
          scale: 1,
        })),
      ],
      actions: [
        {
          objectId: 0,
          type: "move",
          toX: startX + 1 * (barWidth + spacing),
          toY: baseY - values[0] * 15,
        },
        {
          objectId: 1,
          type: "move",
          toX: startX + 0 * (barWidth + spacing),
          toY: baseY - values[1] * 15,
        },
      ],
    },
    // Final sorted highlight
    {
      id: 2,
      duration: 2000,
      objects: [1, 2, 3, 4, 5, 7].map((val, i) => ({
        id: i,
        type: "rect",
        x: startX + i * (barWidth + spacing),
        y: baseY - val * 15,
        width: barWidth,
        height: val * 30,
        color: "#10b981",
        label: val.toString(),
        scale: 1,
      })),
      actions: [1, 2, 3, 4, 5, 7].map((_, i) => ({
        objectId: i,
        type: "highlight",
      })),
    },
  ];
};

const vectorAdditionScenes = (): Scene[] => {
  return [
    // Vector A
    {
      id: 0,
      duration: 1500,
      objects: [
        {
          id: 0,
          type: "arrow",
          startX: 100,
          startY: 300,
          x: 250,
          y: 200,
          color: "#22d3ee",
          label: "A",
        },
        {
          id: 1,
          type: "text",
          x: 300,
          y: 250,
          label: "Vector A",
          color: "#22d3ee",
          size: 18,
        },
      ],
      actions: [{ objectId: 0, type: "fadeIn" }],
    },
    // Vector B appears
    {
      id: 1,
      duration: 1500,
      objects: [
        {
          id: 0,
          type: "arrow",
          startX: 100,
          startY: 300,
          x: 250,
          y: 200,
          color: "#22d3ee",
          label: "A",
        },
        {
          id: 2,
          type: "arrow",
          startX: 250,
          startY: 200,
          x: 400,
          y: 180,
          color: "#a855f7",
          label: "B",
        },
        {
          id: 3,
          type: "text",
          x: 450,
          y: 190,
          label: "Vector B",
          color: "#a855f7",
          size: 18,
        },
      ],
      actions: [{ objectId: 2, type: "fadeIn" }],
    },
    // Resultant vector A+B
    {
      id: 2,
      duration: 2000,
      objects: [
        {
          id: 0,
          type: "arrow",
          startX: 100,
          startY: 300,
          x: 250,
          y: 200,
          color: "#22d3ee",
          label: "A",
        },
        {
          id: 2,
          type: "arrow",
          startX: 250,
          startY: 200,
          x: 400,
          y: 180,
          color: "#a855f7",
          label: "B",
        },
        {
          id: 4,
          type: "arrow",
          startX: 100,
          startY: 300,
          x: 400,
          y: 180,
          color: "#f97316",
          label: "A + B",
        },
        {
          id: 5,
          type: "text",
          x: 300,
          y: 350,
          label: "Resultant: A + B",
          color: "#f97316",
          size: 20,
        },
      ],
      actions: [{ objectId: 4, type: "fadeIn" }],
    },
  ];
};

const pythagorasScenes = (): Scene[] => {
  return [
    // Triangle appears
    {
      id: 0,
      duration: 1500,
      objects: [
        {
          id: 0,
          type: "line",
          startX: 150,
          startY: 300,
          x: 450,
          y: 300,
          color: "#22d3ee",
          width: 3,
        },
        {
          id: 1,
          type: "line",
          startX: 450,
          startY: 300,
          x: 450,
          y: 100,
          color: "#22d3ee",
          width: 3,
        },
        {
          id: 2,
          type: "line",
          startX: 150,
          startY: 300,
          x: 450,
          y: 100,
          color: "#22d3ee",
          width: 3,
        },
        {
          id: 3,
          type: "text",
          x: 300,
          y: 330,
          label: "a = 3",
          color: "#22d3ee",
          size: 16,
        },
        {
          id: 4,
          type: "text",
          x: 480,
          y: 200,
          label: "b = 4",
          color: "#22d3ee",
          size: 16,
        },
      ],
      actions: [
        { objectId: 0, type: "fadeIn" },
        { objectId: 1, type: "fadeIn" },
        { objectId: 2, type: "fadeIn" },
      ],
    },
    // Squares on sides appear
    {
      id: 1,
      duration: 2000,
      objects: [
        {
          id: 0,
          type: "line",
          startX: 150,
          startY: 300,
          x: 450,
          y: 300,
          color: "#22d3ee",
          width: 3,
        },
        {
          id: 1,
          type: "line",
          startX: 450,
          startY: 300,
          x: 450,
          y: 100,
          color: "#22d3ee",
          width: 3,
        },
        {
          id: 2,
          type: "line",
          startX: 150,
          startY: 300,
          x: 450,
          y: 100,
          color: "#22d3ee",
          width: 3,
        },
        {
          id: 5,
          type: "rect",
          x: 300,
          y: 350,
          width: 90,
          height: 90,
          color: "#22d3ee88",
          label: "a²",
          scale: 1,
        },
        {
          id: 6,
          type: "rect",
          x: 500,
          y: 200,
          width: 120,
          height: 120,
          color: "#a855f788",
          label: "b²",
          scale: 1,
        },
      ],
      actions: [
        { objectId: 5, type: "scale", toScale: 1 },
        { objectId: 6, type: "scale", toScale: 1 },
      ],
    },
    // Hypotenuse square
    {
      id: 2,
      duration: 2000,
      objects: [
        {
          id: 0,
          type: "line",
          startX: 150,
          startY: 300,
          x: 450,
          y: 300,
          color: "#22d3ee",
          width: 3,
        },
        {
          id: 1,
          type: "line",
          startX: 450,
          startY: 300,
          x: 450,
          y: 100,
          color: "#22d3ee",
          width: 3,
        },
        {
          id: 2,
          type: "line",
          startX: 150,
          startY: 300,
          x: 450,
          y: 100,
          color: "#f97316",
          width: 4,
        },
        {
          id: 7,
          type: "rect",
          x: 250,
          y: 150,
          width: 150,
          height: 150,
          color: "#f9731688",
          label: "c² = a² + b²",
          scale: 1,
        },
        {
          id: 8,
          type: "text",
          x: 300,
          y: 50,
          label: "c = 5",
          color: "#f97316",
          size: 20,
        },
      ],
      actions: [{ objectId: 7, type: "fadeIn" }],
    },
  ];
};

const binaryTreeScenes = (): Scene[] => {
  return [
    // Root node
    {
      id: 0,
      duration: 1500,
      objects: [
        {
          id: 0,
          type: "circle",
          x: 300,
          y: 100,
          radius: 30,
          color: "#22d3ee",
          label: "5",
          scale: 1,
        },
      ],
      actions: [{ objectId: 0, type: "scale", toScale: 1 }],
    },
    // Add 3 (left)
    {
      id: 1,
      duration: 2000,
      objects: [
        {
          id: 0,
          type: "circle",
          x: 300,
          y: 100,
          radius: 30,
          color: "#22d3ee",
          label: "5",
          scale: 1,
        },
        {
          id: 1,
          type: "line",
          startX: 300,
          startY: 130,
          x: 200,
          y: 180,
          color: "#22d3ee",
        },
        {
          id: 2,
          type: "circle",
          x: 200,
          y: 200,
          radius: 30,
          color: "#f97316",
          label: "3",
          scale: 1,
        },
      ],
      actions: [
        { objectId: 1, type: "fadeIn" },
        { objectId: 2, type: "fadeIn" },
      ],
    },
    // Add 1 (left of 3)
    {
      id: 2,
      duration: 2000,
      objects: [
        {
          id: 0,
          type: "circle",
          x: 300,
          y: 100,
          radius: 30,
          color: "#22d3ee",
          label: "5",
          scale: 1,
        },
        {
          id: 1,
          type: "line",
          startX: 300,
          startY: 130,
          x: 200,
          y: 180,
          color: "#22d3ee",
        },
        {
          id: 2,
          type: "circle",
          x: 200,
          y: 200,
          radius: 30,
          color: "#22d3ee",
          label: "3",
          scale: 1,
        },
        {
          id: 3,
          type: "line",
          startX: 200,
          startY: 230,
          x: 150,
          y: 280,
          color: "#22d3ee",
        },
        {
          id: 4,
          type: "circle",
          x: 150,
          y: 300,
          radius: 30,
          color: "#10b981",
          label: "1",
          scale: 1,
        },
      ],
      actions: [
        { objectId: 3, type: "fadeIn" },
        { objectId: 4, type: "fadeIn" },
      ],
    },
  ];
};

const matrixMultiplyScenes = (): Scene[] => {
  return [
    // Matrix A
    {
      id: 0,
      duration: 1500,
      objects: [
        {
          id: 0,
          type: "rect",
          x: 150,
          y: 150,
          width: 120,
          height: 120,
          color: "#22d3ee88",
          label: "A\n[2x2]",
          scale: 1,
        },
        {
          id: 1,
          type: "text",
          x: 150,
          y: 100,
          label: "Matrix A",
          color: "#22d3ee",
          size: 18,
        },
      ],
      actions: [{ objectId: 0, type: "fadeIn" }],
    },
    // Matrix B appears
    {
      id: 1,
      duration: 1500,
      objects: [
        {
          id: 0,
          type: "rect",
          x: 150,
          y: 150,
          width: 120,
          height: 120,
          color: "#22d3ee88",
          label: "A\n[2x2]",
          scale: 1,
        },
        {
          id: 2,
          type: "rect",
          x: 350,
          y: 150,
          width: 120,
          height: 120,
          color: "#a855f788",
          label: "B\n[2x2]",
          scale: 1,
        },
        {
          id: 3,
          type: "text",
          x: 350,
          y: 100,
          label: "Matrix B",
          color: "#a855f7",
          size: 18,
        },
        {
          id: 4,
          type: "text",
          x: 250,
          y: 150,
          label: "×",
          color: "#fff",
          size: 32,
        },
      ],
      actions: [{ objectId: 2, type: "fadeIn" }],
    },
    // Result matrix
    {
      id: 2,
      duration: 2000,
      objects: [
        {
          id: 0,
          type: "rect",
          x: 150,
          y: 150,
          width: 120,
          height: 120,
          color: "#22d3ee88",
          label: "A\n[2x2]",
          scale: 1,
        },
        {
          id: 2,
          type: "rect",
          x: 350,
          y: 150,
          width: 120,
          height: 120,
          color: "#a855f788",
          label: "B\n[2x2]",
          scale: 1,
        },
        {
          id: 4,
          type: "text",
          x: 250,
          y: 150,
          label: "×",
          color: "#fff",
          size: 32,
        },
        {
          id: 5,
          type: "text",
          x: 430,
          y: 150,
          label: "=",
          color: "#fff",
          size: 32,
        },
        {
          id: 6,
          type: "rect",
          x: 520,
          y: 150,
          width: 120,
          height: 120,
          color: "#f9731688",
          label: "A×B\n[2x2]",
          scale: 1,
        },
        {
          id: 7,
          type: "text",
          x: 520,
          y: 100,
          label: "Result",
          color: "#f97316",
          size: 18,
        },
      ],
      actions: [
        { objectId: 6, type: "fadeIn" },
        { objectId: 7, type: "fadeIn" },
      ],
    },
  ];
};

const defaultGraphScenes = (): Scene[] => {
  return [
    {
      id: 0,
      duration: 2000,
      objects: [
        {
          id: 0,
          type: "text",
          x: 300,
          y: 150,
          label: "Concept Visualization",
          color: "#22d3ee",
          size: 24,
        },
        {
          id: 1,
          type: "circle",
          x: 300,
          y: 250,
          radius: 50,
          color: "#22d3ee88",
          label: "Node",
          scale: 1,
        },
      ],
      actions: [
        { objectId: 0, type: "fadeIn" },
        { objectId: 1, type: "scale", toScale: 1 },
      ],
    },
  ];
};
