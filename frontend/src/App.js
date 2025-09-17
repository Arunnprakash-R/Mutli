import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [language, setLanguage] = useState('es');
  const [translatedText, setTranslatedText] = useState('');
  const [error, setError] = useState('');

  const fetchTranslation = async (lang) => {
    try {
      const response = await fetch(`http://localhost:5000/translate?text=Welcome&lang=${lang}`);
      const data = await response.json();
      if (response.ok) {
        setTranslatedText(data.translated_text);
        setError('');
      } else {
        setError(data.error || 'An error occurred.');
        setTranslatedText('');
      }
    } catch (error) {
      console.error("Error fetching translation:", error);
      setError("Error fetching translation. Make sure the backend server is running.");
      setTranslatedText('');
    }
  };

  useEffect(() => {
    fetchTranslation(language);
  }, [language]);

  const handleTranslate = () => {
    const langInput = document.getElementById('language-input');
    if (langInput) {
      setLanguage(langInput.value);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome Translator</h1>
        <div className="input-container">
          <input
            id="language-input"
            type="text"
            placeholder="Enter language (e.g., es, fr, de)"
            defaultValue={language}
          />
          <button onClick={handleTranslate}>Translate</button>
        </div>
        <div className="translation-container">
          {error ? (
            <p className="error-text">{error}</p>
          ) : (
            <>
              <h2>Translated "Welcome":</h2>
              <p className="translated-text">{translatedText}</p>
            </>
          )}
        </div>
      </header>
    </div>
  );
}

export default App;
