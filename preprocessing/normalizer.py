def normalize_to_english(text, language, llm=None):
    """
    If text is already English, return as-is.
    If Hindi, it will later be translated using LLM.
    """
    if language == "en":
        return text

    if language == "hi":
        return "[HINDI CONTRACT - TRANSLATION PENDING]\n" + text

    return text
