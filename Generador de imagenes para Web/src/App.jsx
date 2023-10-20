import { uploadFile } from "./firebase/config";
import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [imageURL, setImageURL] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleCopyLink = () => {
    if (imageURL) {
      const el = document.createElement("textarea");
      el.value = imageURL;
      document.body.appendChild(el);
      el.select();
      document.execCommand("copy");
      document.body.removeChild(el);
      alert("Enlace copiado en el portapapeles");
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const generatedLink = await uploadFile(file);
      setImageURL(generatedLink);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          name=""
          id="input"
          onChange={handleFileChange}
        />
        <button>Generar Link</button>
      </form>

      {imageURL && (
        <div>
          <div id="imagenDiv">
            <img id="imagenMostrada" src={imageURL} alt="Imagen cargada" width="300px" />
          </div>
          <button onClick={handleCopyLink}>Copiar Enlace</button>
        </div>
      )}

      {/* Mostrar mensaje cuando no se ha cargado una imagen */}
      {!imageURL && (
        <p id="textoCuandoNoHayImagen"> Se mostrará la imagen cuando la misma se guarde correctamente </p>
      )}
    </div>
  );
}

export default App;
