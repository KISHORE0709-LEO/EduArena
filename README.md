# EduArena - Text-to-Animation Platform

A modern SaaS platform that transforms natural language descriptions of educational concepts into beautiful, interactive animations. Built with React, TypeScript, and Tailwind CSS.

## 🚀 Features

### Core Functionality
- **Text-to-Animation Generation**: Convert natural language descriptions into structured animation scenes
- **Real-time Preview**: Watch animations render in real-time with smooth 60fps performance
- **Interactive Canvas**: Dynamic animation canvas with play/pause controls and speed adjustment
- **Template Library**: 15+ pre-built templates for sorting algorithms, data structures, math concepts, and more

### User Interface
- **Dark Cyber Theme**: Futuristic design with cyan/blue accents and glowing effects
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **3D Robot Assistant**: Interactive Spline 3D model on the landing page
- **Glassmorphism UI**: Modern glass-panel effects with backdrop blur

### Navigation & Pages
- **Landing Page**: Hero section with 3D robot, feature highlights, and demo video
- **Main App**: Full animation studio with navbar, templates, and generation tools
- **Product Page**: Feature showcase and capabilities overview
- **How It Works**: Step-by-step process explanation
- **Templates**: Browse animation template library
- **Documentation**: Complete guides and API references
- **Profile**: Student dashboard with progress tracking

## 🛠️ Tech Stack

- **Frontend**: React 18, TypeScript, Vite
- **Styling**: Tailwind CSS, shadcn/ui components
- **3D Graphics**: Spline (for 3D robot model)
- **Routing**: React Router DOM
- **State Management**: React hooks
- **Icons**: Lucide React
- **Animations**: CSS animations with Tailwind

## 📁 Project Structure

```
src/
├── components/
│   ├── ui/                 # shadcn/ui components
│   ├── AnimationCanvas.tsx # Main animation renderer
│   ├── AnimationGallery.tsx# Template gallery
│   ├── HeroSection.tsx     # Landing hero section
│   ├── Navbar.tsx          # Navigation component
│   └── OutputPanel.tsx     # Animation output display
├── pages/
│   ├── Landing.tsx         # Landing page
│   ├── Index.tsx           # Main app page
│   ├── Product.tsx         # Product features
│   ├── HowItWorks.tsx      # Process explanation
│   ├── Templates.tsx       # Template library
│   ├── Docs.tsx            # Documentation
│   ├── Profile.tsx         # User profile
│   ├── SignIn.tsx          # Authentication
│   └── SignUp.tsx          # User registration
├── lib/
│   ├── sceneTemplates.ts   # Animation scene generation
│   └── utils.ts            # Utility functions
└── hooks/                  # Custom React hooks
```

## 🎨 Design System

### Colors
- **Primary**: Cyan (#00E5FF) to Blue (#2196F3) gradients
- **Accent**: Yellow (#FFC107) for highlights
- **Background**: Dark navy/black gradients
- **Text**: White primary, gray secondary

### Components
- **Buttons**: Gradient backgrounds with glow effects
- **Cards**: Glass panels with cyan borders
- **Inputs**: Dark backgrounds with cyan focus states
- **Navigation**: Pill-shaped capsule with active states

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ and npm
- Modern web browser with ES6+ support

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd educanvas-animator
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:8081`

### Build for Production
```bash
npm run build
```

## 📱 Usage

### Creating Animations

1. **Navigate to the App**: Click "Enter the Arena" from the landing page
2. **Choose Input Method**:
   - Type a custom description in the text area
   - Select from example prompts dropdown
   - Click on pre-built templates
3. **Generate**: Click "Generate Animation" to create your animation
4. **Control Playback**: Use play/pause, restart, and speed controls
5. **View Code**: Toggle between input text and generated JSON

### Example Prompts
- "bubble sort 6 numbers"
- "vector addition with two arrows"
- "binary search tree insert"
- "Pythagoras theorem visualization"
- "merge sort algorithm"

### Navigation
- **HOME**: Returns to main app
- **PRODUCT**: Feature overview
- **HOW IT WORKS**: Process explanation
- **TEMPLATES**: Browse template library
- **DOCS**: Documentation and guides
- **GITHUB**: Source code repository
- **PROFILE**: User dashboard

## 🎯 Supported Concepts

### Algorithms
- Sorting: Bubble, Merge, Quick, Selection
- Search: Binary Search, Linear Search
- Graph: BFS, DFS traversal

### Data Structures
- Linked Lists, Stacks, Queues
- Binary Trees, Binary Search Trees
- Arrays and dynamic operations

### Mathematics
- Vector operations and visualization
- Geometric theorems (Pythagoras)
- Matrix operations
- Calculus concepts (derivatives)

### Physics
- Motion and kinematics
- Force diagrams
- Wave animations

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:
```env
VITE_APP_TITLE=EduArena
VITE_SPLINE_SCENE_URL=https://prod.spline.design/rU2-Ks0SC0T5od9B/scene.splinecode
```

### Customization
- **Colors**: Modify `src/index.css` CSS variables
- **Templates**: Add new templates in `src/lib/sceneTemplates.ts`
- **Components**: Extend UI components in `src/components/ui/`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **shadcn/ui** for the component library
- **Spline** for 3D graphics capabilities
- **Lucide** for the icon system
- **Tailwind CSS** for styling framework

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation at `/docs`
- Visit the How It Works page for guidance

---

Built with ❤️ for educational content creators and learners worldwide.