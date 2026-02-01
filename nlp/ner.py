import spacy
from spacy.pipeline import EntityRuler

# Create a lightweight English pipeline (NO external model)
nlp = spacy.blank("en")

# Add EntityRuler for rule-based NER
ruler = nlp.add_pipe("entity_ruler")

# Basic legal / contract entity patterns
patterns = [
    # Money
    {"label": "MONEY", "pattern": [{"TEXT": {"REGEX": "INR|Rs\\.?|₹"}}, {"IS_DIGIT": True}]},
    {"label": "MONEY", "pattern": [{"IS_DIGIT": True}, {"LOWER": "lakhs"}]},
    {"label": "MONEY", "pattern": [{"IS_DIGIT": True}, {"LOWER": "crores"}]},

    # Dates
    {"label": "DATE", "pattern": [{"IS_DIGIT": True}, {"LOWER": {"IN": ["days", "months", "years"]}}]},
    {"label": "DATE", "pattern": [{"IS_DIGIT": True}, {"IS_ALPHA": True}, {"IS_DIGIT": True}]},

    # Organizations
    {"label": "ORG", "pattern": [{"IS_TITLE": True}, {"IS_TITLE": True}, {"LOWER": {"IN": ["pvt", "ltd", "limited"]}}]},
    {"label": "ORG", "pattern": [{"IS_TITLE": True}, {"LOWER": "technologies"}]},

    # Locations / Jurisdiction
    {"label": "GPE", "pattern": [{"IS_TITLE": True}]}
]

ruler.add_patterns(patterns)


def extract_entities(text):
    """
    Extract entities using rule-based spaCy pipeline.
    Cloud-safe (no model downloads).
    """
    doc = nlp(text)

    entities = []
    for ent in doc.ents:
        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities
