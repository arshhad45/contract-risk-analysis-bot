import spacy
from spacy.pipeline import EntityRuler
from functools import lru_cache


@lru_cache(maxsize=1)
def get_nlp():
    nlp = spacy.blank("en")
    ruler = nlp.add_pipe("entity_ruler")

    patterns = [
        {"label": "MONEY", "pattern": [{"TEXT": {"REGEX": "INR|Rs\\.?|₹"}}, {"IS_DIGIT": True}]},
        {"label": "DATE", "pattern": [{"IS_DIGIT": True}, {"LOWER": {"IN": ["days", "months", "years"]}}]},
        {"label": "ORG", "pattern": [{"IS_TITLE": True}, {"IS_TITLE": True}]},
        {"label": "GPE", "pattern": [{"IS_TITLE": True}]}
    ]

    ruler.add_patterns(patterns)
    return nlp


def extract_entities(text):
    nlp = get_nlp()
    doc = nlp(text)

    return [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
