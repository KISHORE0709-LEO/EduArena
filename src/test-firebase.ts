import { auth, db } from './lib/firebase';
import { createUserWithEmailAndPassword } from 'firebase/auth';
import { doc, setDoc } from 'firebase/firestore';

const testFirebase = async () => {
  try {
    // Create test user
    const userCredential = await createUserWithEmailAndPassword(auth, 'test@example.com', 'password123');
    const user = userCredential.user;
    console.log('Created user:', user.uid);

    // Test creating a user document
    await setDoc(doc(db, 'users', user.uid), {
      email: 'test@example.com',
      name: 'Test User',
      role: 'student',
      createdAt: new Date(),
      updatedAt: new Date()
    });

    console.log('Firebase setup successful!');
  } catch (error) {
    console.error('Firebase test failed:', error);
  }
};

testFirebase();