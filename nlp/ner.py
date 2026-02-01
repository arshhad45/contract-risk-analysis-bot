import spacy

# Load spaCy model safely (local + Streamlit Cloud)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # If model is not present (e.g., Streamlit Cloud)
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    """
    Extract named entities from text using spaCy.
    Returns a list of dictionaries with entity text and label.
    """
    doc = nlp(text)

    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities
