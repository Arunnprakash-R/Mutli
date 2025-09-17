from deep_translator import GoogleTranslator

def translate_text(text, target_language):
    """
    Translates the given text to the target language using deep-translator.
    """
    if not text:
        return ""
    try:
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated
    except Exception as e:
        print(f"Error during translation: {e}")
        return "Error: Translation failed."
