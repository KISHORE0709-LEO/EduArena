import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Link, useNavigate } from "react-router-dom";
import { Sparkles } from "lucide-react";
import { useState } from "react";
import { createUserWithEmailAndPassword } from "firebase/auth";
import { doc, setDoc } from "firebase/firestore";
import { auth, db } from "@/lib/firebase";

const SignUp = () => {
  const [formData, setFormData] = useState({ name: '', email: '', password: '', role: '' });
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      // Create user account
      const userCredential = await createUserWithEmailAndPassword(auth, formData.email, formData.password);
      const user = userCredential.user;
      
      // Save user data to Firestore
      await setDoc(doc(db, 'users', user.uid), {
        email: formData.email,
        name: formData.name,
        role: formData.role,
        createdAt: new Date(),
        updatedAt: new Date()
      });
      
      // Create user profile
      await setDoc(doc(db, 'user_profiles', user.uid), {
        userId: user.uid,
        animationsCreated: 0,
        conceptsLearned: 0,
        studyTime: 0,
        avatar: formData.name.split(' ').map(n => n[0]).join('').toUpperCase(),
        bio: `${formData.role.charAt(0).toUpperCase() + formData.role.slice(1)}`,
        createdAt: new Date(),
        updatedAt: new Date()
      });
      
      console.log('User created successfully:', user.uid);
      console.log('Collections created: users, user_profiles');
      
      navigate('/app');
    } catch (error) {
      console.error('Signup error:', error);
      alert('Signup failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };
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

      {/* Sign Up Card */}
      <Card className="w-full max-w-md bg-slate-900/90 backdrop-blur-xl border-slate-700/50 relative z-10 shadow-2xl">
        <div className="absolute inset-0 bg-gradient-to-br from-cyan-500/5 to-yellow-500/5 rounded-lg" />
        
        <CardHeader className="relative z-10 text-center space-y-2">
          <CardTitle className="text-2xl font-bold text-white">Create your EduArena account</CardTitle>
          <CardDescription className="text-gray-400">
            Join the future of educational content creation
          </CardDescription>
        </CardHeader>
        
        <CardContent className="relative z-10 space-y-6">
          <form className="space-y-4" onSubmit={handleSubmit}>
            <div className="space-y-2">
              <Label htmlFor="name" className="text-gray-300">Full Name</Label>
              <Input
                id="name"
                type="text"
                placeholder="Enter your full name"
                value={formData.name}
                onChange={(e) => setFormData({...formData, name: e.target.value})}
                required
                className="bg-slate-800/70 border-slate-600 text-white placeholder:text-gray-500 focus:border-cyan-400 focus:ring-cyan-400/20"
              />
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="email" className="text-gray-300">Email</Label>
              <Input
                id="email"
                type="email"
                placeholder="Enter your email"
                value={formData.email}
                onChange={(e) => setFormData({...formData, email: e.target.value})}
                required
                className="bg-slate-800/70 border-slate-600 text-white placeholder:text-gray-500 focus:border-cyan-400 focus:ring-cyan-400/20"
              />
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="password" className="text-gray-300">Password</Label>
              <Input
                id="password"
                type="password"
                placeholder="Create a password"
                value={formData.password}
                onChange={(e) => setFormData({...formData, password: e.target.value})}
                required
                minLength={6}
                className="bg-slate-800/70 border-slate-600 text-white placeholder:text-gray-500 focus:border-cyan-400 focus:ring-cyan-400/20"
              />
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="role" className="text-gray-300">Role</Label>
              <Select value={formData.role} onValueChange={(value) => setFormData({...formData, role: value})} required>
                <SelectTrigger className="bg-slate-800/70 border-slate-600 text-white focus:border-cyan-400 focus:ring-cyan-400/20">
                  <SelectValue placeholder="Select your role" />
                </SelectTrigger>
                <SelectContent className="bg-slate-800 border-slate-600">
                  <SelectItem value="student" className="text-white hover:bg-slate-700">Student</SelectItem>
                  <SelectItem value="teacher" className="text-white hover:bg-slate-700">Teacher</SelectItem>
                  <SelectItem value="creator" className="text-white hover:bg-slate-700">Creator</SelectItem>
                </SelectContent>
              </Select>
            </div>
            
            <Button 
              type="submit" 
              disabled={loading}
              className="w-full bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white font-semibold py-3 shadow-lg shadow-cyan-500/25 disabled:opacity-50"
            >
              {loading ? 'Creating Account...' : 'Create Account'}
            </Button>
          </form>
          
          <div className="text-center">
            <div className="text-sm text-gray-400">
              Already have an account?{" "}
              <Link to="/signin" className="text-cyan-400 hover:text-cyan-300">
                Sign in
              </Link>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default SignUp;