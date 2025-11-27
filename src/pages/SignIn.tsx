import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Link } from "react-router-dom";
import { Sparkles } from "lucide-react";

const SignIn = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-black flex items-center justify-center p-6">
      {/* Grid Background */}
      <div className="absolute inset-0 bg-[linear-gradient(rgba(6,182,212,0.08)_1px,transparent_1px),linear-gradient(90deg,rgba(6,182,212,0.08)_1px,transparent_1px)] bg-[size:50px_50px]" />
      
      {/* Background Effects */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-[400px] h-[400px] bg-cyan-500/15 rounded-full blur-3xl animate-pulse" />
        <div className="absolute bottom-1/4 right-1/4 w-[400px] h-[400px] bg-yellow-500/10 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }} />
      </div>

      {/* Logo */}
      <Link to="/" className="absolute top-6 left-6 flex items-center gap-3 z-20">
        <div className="w-10 h-10 bg-gradient-to-r from-cyan-400 to-blue-500 rounded-full flex items-center justify-center">
          <Sparkles className="w-6 h-6 text-white" />
        </div>
        <span className="text-xl font-bold text-white">EduArena</span>
      </Link>

      {/* Sign In Card */}
      <Card className="w-full max-w-md bg-slate-900/90 backdrop-blur-xl border-slate-700/50 relative z-10 shadow-2xl">
        <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/5 to-yellow-500/5 rounded-lg" />
        
        <CardHeader className="relative z-10 text-center space-y-2">
          <CardTitle className="text-2xl font-bold text-white">Sign In</CardTitle>
          <CardDescription className="text-gray-400">
            Welcome back to EduArena
          </CardDescription>
        </CardHeader>
        
        <CardContent className="relative z-10 space-y-6">
          <form className="space-y-4" onSubmit={(e) => { e.preventDefault(); window.location.href = '/app'; }}>
            <div className="space-y-2">
              <Label htmlFor="email" className="text-gray-300">Email</Label>
              <Input
                id="email"
                type="email"
                placeholder="Enter your email"
                className="bg-slate-800/70 border-slate-600 text-white placeholder:text-gray-500 focus:border-cyan-400 focus:ring-cyan-400/20"
              />
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="password" className="text-gray-300">Password</Label>
              <Input
                id="password"
                type="password"
                placeholder="Enter your password"
                className="bg-slate-800/70 border-slate-600 text-white placeholder:text-gray-500 focus:border-cyan-400 focus:ring-cyan-400/20"
              />
            </div>
            
            <Button 
              type="submit" 
              className="w-full bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white font-semibold py-3 shadow-lg shadow-cyan-500/25"
            >
              Sign In
            </Button>
          </form>
          
          <div className="text-center space-y-2">
            <Link to="/forgot-password" className="text-sm text-yellow-400 hover:text-yellow-300">
              Forgot your password?
            </Link>
            <div className="text-sm text-gray-400">
              Don't have an account?{" "}
              <Link to="/signup" className="text-cyan-400 hover:text-cyan-300">
                Sign up
              </Link>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default SignIn;