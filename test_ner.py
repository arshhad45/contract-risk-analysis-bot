from nlp.ner import extract_entities

sample_clause = """
The Client shall pay INR 50,000 to ABC Technologies Pvt Ltd
within 15 days from 1 January 2024.
"""

entities = extract_entities(sample_clause)

print("Extracted Entities:")
for e in entities:
    print(f"{e['text']}  -->  {e['label']}")

