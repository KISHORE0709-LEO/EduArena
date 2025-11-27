import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyCyr8rCuf03YVZteetwXUYtw0HU6LO8JIc",
  authDomain: "eduarena-684d9.firebaseapp.com",
  projectId: "eduarena-684d9",
  storageBucket: "eduarena-684d9.firebasestorage.app",
  messagingSenderId: "812813644008",
  appId: "1:812813644008:web:c814060bd622635ad1195d"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
export default app;