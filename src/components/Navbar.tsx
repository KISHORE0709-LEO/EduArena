import { Button } from "@/components/ui/button";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { Sparkles, LogOut } from "lucide-react";
import { useAuth } from "@/contexts/AuthContext";

const Navbar = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { user, logout } = useAuth();

  const handleLogout = async () => {
    await logout();
    navigate('/');
  };
  const navItems = [
    { label: "HOME", href: "/app" },
    { label: "PRODUCT", href: "/product" },
    { label: "HOW IT WORKS", href: "/how-it-works" },
    { label: "TEMPLATES", href: "/templates" },
    { label: "DOCS", href: "/docs" },
    { label: "GITHUB", href: "https://github.com" }
  ];

  return (
    <nav className="flex items-center justify-between w-full px-6 py-4">
      {/* Logo */}
      <Link to="/" className="flex items-center gap-3">
        <div className="w-10 h-10 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-full flex items-center justify-center">
          <Sparkles className="w-6 h-6 text-white" />
        </div>
        <span className="text-xl font-bold text-white">EduArena</span>
      </Link>

      {/* Center Navigation Capsule */}
      <div className="flex items-center justify-center flex-1">
        <div className="flex items-center bg-transparent border-2 border-cyan-400/60 hover:border-cyan-300/80 rounded-full px-2 py-2 gap-1 shadow-xl shadow-cyan-400/30">
          {navItems.map((item, index) => (
            <Link
              key={index}
              to={item.href}
              className={`px-4 py-2 text-sm font-semibold rounded-full transition-all ${
                location.pathname === item.href
                  ? "bg-gradient-to-r from-cyan-500 to-blue-600 text-white"
                  : "text-gray-300 hover:text-white"
              }`}
            >
              {item.label}
            </Link>
          ))}
        </div>
      </div>

      {/* Profile & Auth Buttons */}
      <div className="flex items-center gap-3">
        {user ? (
          <>
            <Link to="/profile">
              <Button className="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white font-semibold px-6 py-2 rounded-full">
                PROFILE
              </Button>
            </Link>
            <Button 
              onClick={handleLogout}
              variant="outline"
              className="border-cyan-400 text-cyan-400 hover:bg-cyan-400 hover:text-black px-4 py-2 rounded-full"
            >
              <LogOut className="w-4 h-4" />
            </Button>
          </>
        ) : (
          <Link to="/signin">
            <Button className="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white font-semibold px-6 py-2 rounded-full">
              SIGN IN
            </Button>
          </Link>
        )}
      </div>
    </nav>
  );
};

export default Navbar;