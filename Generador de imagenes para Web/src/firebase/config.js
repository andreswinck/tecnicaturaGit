import { initializeApp } from "firebase/app";
import {getStorage, ref, uploadBytes, getDownloadURL} from 'firebase/storage';
import {v4} from 'uuid'

const firebaseConfig = {
  apiKey: "AIzaSyB97ydIaSFwsjC8jVdMGnw0a4ZjWs7xTDA",
  authDomain: "imagenes-blog-38046.firebaseapp.com",
  projectId: "imagenes-blog-38046",
  storageBucket: "imagenes-blog-38046.appspot.com",
  messagingSenderId: "879887629021",
  appId: "1:879887629021:web:70329c852ad062177a3934"
};

const app = initializeApp(firebaseConfig);
export const storage = getStorage(app);

export async function uploadFile(file){
    const storageRef = ref(storage, v4())
    await uploadBytes(storageRef, file)
    const url = getDownloadURL(storageRef)
    return url

}

