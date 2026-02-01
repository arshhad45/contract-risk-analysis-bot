from nlp.clause_splitter import split_clauses
from nlp.intent import detect_intent

text = """
1. Payment
The Client shall pay INR 50,000 within 15 days.

2. Termination
The Company may terminate this agreement at its sole discretion.

3. Confidentiality
The Employee shall not disclose confidential information.
"""

clauses = split_clauses(text)

for c in clauses:
    print("\n---------------------")
    print("Clause Text:")
    print(c["text"])
    print("Detected Intent:", detect_intent(c["text"]))
