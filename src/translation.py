from googletrans import Translator

def translate_text(text, target_language):
    """
    Translates the given text to the target language.
    """
    if not text:
        return ""
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text
