from nlp.clause_splitter import split_clauses

sample_text = """
1. Termination
Either party may terminate this agreement with 30 days written notice.

2. Payment Terms
The client shall pay INR 50,000 within 15 days of invoice.

3. Confidentiality
The parties shall maintain confidentiality of all shared information.
"""

clauses = split_clauses(sample_text)

for clause in clauses:
    print("\n----------------------")
    print("Clause ID:", clause["clause_id"])
    print("Clause Text:")
    print(clause["text"])
