from preprocessing.language import detect_language
from preprocessing.normalizer import normalize_to_english

english_text = """
This Agreement may be terminated by either party with 30 days notice.
"""

hindi_text = """
यह समझौता किसी भी पक्ष द्वारा 30 दिनों की सूचना देकर समाप्त किया जा सकता है।
"""

for text in [english_text, hindi_text]:
    lang = detect_language(text)
    normalized = normalize_to_english(text, lang)

    print("\n====================")
    print("Detected Language:", lang)
    print("Normalized Output:")
    print(normalized)
