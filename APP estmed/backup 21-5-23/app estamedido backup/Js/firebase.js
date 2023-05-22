// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
//autoautenticacion
import { getAuth } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-auth.js";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB_AAeNsfOx06T3cQs1RUO1mDMRKOzRDq0",
  authDomain: "proyecto-app-estacionamiento.firebaseapp.com",
  projectId: "proyecto-app-estacionamiento",
  storageBucket: "proyecto-app-estacionamiento.appspot.com",
  messagingSenderId: "166187970469",
  appId: "1:166187970469:web:e94074c2a0b547b10a024c",
  measurementId: "G-RL78P7N5DC"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const auth = getAuth(app);