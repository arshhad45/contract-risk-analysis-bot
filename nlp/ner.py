import spacy

# Load once (important for performance later)
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    """
    Extract named entities from text using spaCy.
    Returns a list of (entity_text, entity_label).
    """
    doc = nlp(text)

    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities
