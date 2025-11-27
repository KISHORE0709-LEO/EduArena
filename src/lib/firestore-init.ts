import { collection, doc, setDoc } from 'firebase/firestore';
import { db } from './firebase';

// Initialize Firestore collections with sample data
export const initializeCollections = async () => {
  try {
    // Sample user
    const userRef = doc(db, 'users', 'sample-user-id');
    await setDoc(userRef, {
      email: 'john.student@example.com',
      name: 'John Student',
      role: 'student',
      createdAt: new Date(),
      updatedAt: new Date()
    });

    // Sample user profile
    const profileRef = doc(db, 'user_profiles', 'sample-user-id');
    await setDoc(profileRef, {
      userId: 'sample-user-id',
      animationsCreated: 23,
      conceptsLearned: 15,
      studyTime: 12.5,
      avatar: 'JS',
      bio: 'Computer Science Student',
      createdAt: new Date(),
      updatedAt: new Date()
    });

    // Sample animation
    const animationRef = doc(db, 'animations', 'sample-animation-id');
    await setDoc(animationRef, {
      userId: 'sample-user-id',
      title: 'Bubble Sort Animation',
      description: 'bubble sort 6 numbers',
      animationData: {
        type: 'sorting',
        algorithm: 'bubble',
        elements: [64, 34, 25, 12, 22, 11]
      },
      template: 'bubble-sort',
      createdAt: new Date(),
      isPublic: true
    });

    console.log('Collections initialized successfully');
  } catch (error) {
    console.error('Error initializing collections:', error);
  }
};

// Collection references for easy access
export const collections = {
  users: collection(db, 'users'),
  userProfiles: collection(db, 'user_profiles'),
  animations: collection(db, 'animations')
};