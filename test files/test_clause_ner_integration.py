from nlp.clause_splitter import split_clauses
from nlp.ner import extract_entities

text = """
1. Payment
The Client shall pay INR 50,000 to ABC Technologies Pvt Ltd
within 15 days from 1 January 2024.

2. Termination
Either party may terminate this agreement with 30 days notice.
"""

clauses = split_clauses(text)

for clause in clauses:
    print("\n-----------------------")
    print("Clause ID:", clause["clause_id"])
    print("Clause Text:")
    print(clause["text"])
    print("Entities:")
    print(extract_entities(clause["text"]))
