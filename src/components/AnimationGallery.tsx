import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

interface Template {
  id: string;
  title: string;
  category: string;
  description: string;
  example: string;
}

const templates: Template[] = [
  { id: "bubble", title: "Bubble Sort", category: "Sorting", description: "Visualize bubble sort algorithm", example: "bubble sort 6 numbers" },
  { id: "merge", title: "Merge Sort", category: "Sorting", description: "Divide and conquer sorting", example: "merge sort algorithm" },
  { id: "quick", title: "Quick Sort", category: "Sorting", description: "Pivot-based sorting", example: "quick sort visualization" },
  { id: "selection", title: "Selection Sort", category: "Sorting", description: "Selection sort algorithm", example: "selection sort animation" },
  { id: "linked", title: "Linked List", category: "Data Structures", description: "Linked list operations", example: "linked list insert node" },
  { id: "stack", title: "Stack", category: "Data Structures", description: "LIFO data structure", example: "stack push and pop" },
  { id: "queue", title: "Queue", category: "Data Structures", description: "FIFO data structure", example: "queue enqueue dequeue" },
  { id: "bst", title: "Binary Tree", category: "Data Structures", description: "Binary search tree", example: "binary search tree insert" },
  { id: "bfs", title: "BFS", category: "Graph", description: "Breadth-first search", example: "breadth first search" },
  { id: "dfs", title: "DFS", category: "Graph", description: "Depth-first search", example: "depth first search" },
  { id: "vector", title: "Vector Addition", category: "Math", description: "Vector mathematics", example: "vector addition" },
  { id: "pythagoras", title: "Pythagoras", category: "Math", description: "Pythagorean theorem", example: "Pythagoras theorem" },
  { id: "matrix", title: "Matrix Multiply", category: "Math", description: "Matrix multiplication", example: "matrix 2x2 multiply" },
  { id: "derivative", title: "Derivatives", category: "Math", description: "Calculus derivatives", example: "derivative visualization" },
  { id: "factorial", title: "Factorial", category: "Math", description: "Factorial computation", example: "factorial animation" },
];

interface AnimationGalleryProps {
  onSelect: (example: string) => void;
}

export const AnimationGallery = ({ onSelect }: AnimationGalleryProps) => {
  const categories = Array.from(new Set(templates.map(t => t.category)));

  return (
    <section className="container mx-auto px-4 py-16">
      <div className="max-w-6xl mx-auto space-y-8">
        <div className="text-center space-y-2">
          <h2 className="text-3xl font-bold gradient-text">Animation Templates</h2>
          <p className="text-muted-foreground">15+ pre-built animations across sorting, data structures, graphs, and math</p>
        </div>

        {categories.map((category) => (
          <div key={category} className="space-y-4">
            <h3 className="text-xl font-semibold flex items-center gap-2">
              <Badge variant="outline" className="text-sm border-cyan-400/70 text-cyan-300 shadow-md shadow-cyan-400/20">{category}</Badge>
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {templates
                .filter((t) => t.category === category)
                .map((template) => (
                  <Card
                    key={template.id}
                    className="bg-slate-900/70 border-2 border-cyan-400/60 hover:border-cyan-300 p-4 cursor-pointer hover:scale-105 transition-all rounded-xl shadow-xl shadow-cyan-400/30 hover:shadow-cyan-300/50"
                    onClick={() => onSelect(template.example)}
                  >
                    <div className="space-y-2">
                      <h4 className="font-semibold text-foreground">{template.title}</h4>
                      <p className="text-sm text-muted-foreground">{template.description}</p>
                      <code className="text-xs bg-slate-800/70 border border-cyan-400/50 px-2 py-1 rounded block text-cyan-200 shadow-sm shadow-cyan-400/20">
                        {template.example}
                      </code>
                    </div>
                  </Card>
                ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};
