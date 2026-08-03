from lingua import Language, LanguageDetectorBuilder
from deep_translator import GoogleTranslator

# Supported languages
SUPPORTED_LANGUAGES = {
    "en": "english",
    "hi": "hindi",
    "es": "spanish",
    "fr": "french"
}

# Build Lingua detector
detector = LanguageDetectorBuilder.from_languages(
    Language.ENGLISH,
    Language.HINDI,
    Language.SPANISH,
    Language.FRENCH
).build()


def detect_language(text):
    """
    Detect the language of the input text.
    Returns:
        en, hi, es, fr
    """
    try:
        language = detector.detect_language_of(text)

        if language is None:
            return "en"

        language_map = {
            Language.ENGLISH: "en",
            Language.HINDI: "hi",
            Language.SPANISH: "es",
            Language.FRENCH: "fr"
        }

        return language_map.get(language, "en")

    except Exception:
        return "en"


def translate_to_english(text, source_lang):
    """
    Translate user input to English before sending
    it to the chatbot.
    """
    if source_lang == "en":
        return text

    try:
        return GoogleTranslator(
            source=source_lang,
            target="en"
        ).translate(text)

    except Exception:
        return text


def translate_from_english(text, target_lang):
    """
    Translate chatbot response back to the user's language.
    """
    if target_lang == "en":
        return text

    try:
        return GoogleTranslator(
            source="en",
            target=target_lang
        ).translate(text)

    except Exception:
        return text