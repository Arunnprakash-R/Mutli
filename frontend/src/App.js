import React, { useState } from 'react';
import './App.css';

function App() {
  const [translatedText, setTranslatedText] = useState('');
  const [error, setError] = useState('');
  const [downloadPath, setDownloadPath] = useState('');

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (!file) {
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const uploadResponse = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });

      if (!uploadResponse.ok) {
        throw new Error('File upload failed');
      }

      const uploadData = await uploadResponse.json();
      const { filepath } = uploadData;

      // Now, call translation endpoint
      const translateResponse = await fetch('http://localhost:5000/translate-file', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ filepath, lang: 'en' }), // Hardcoding lang for now
      });

      if (!translateResponse.ok) {
        throw new Error('Translation failed');
      }

      const translateData = await translateResponse.json();
      setTranslatedText(translateData.translated_text);
      setDownloadPath(translateData.download_path);
      setError('');
    } catch (error) {
      console.error("Error:", error);
      setError(error.message || "An error occurred.");
      setTranslatedText('');
      setDownloadPath('');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Document Translator</h1>
      </header>
      <div className="container">
        <div className="panel upload-section">
          <input type="file" onChange={handleFileChange} />
        </div>
        <div className="panel">
          <h2>Translated Text</h2>
          {error && <p className="error-text">{error}</p>}
          <div className="translation-output">{translatedText}</div>
          {downloadPath && (
            <a href={`http://localhost:5000/download/${downloadPath.split('/').pop()}`} download>
              <button>Download as PDF</button>
            </a>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
