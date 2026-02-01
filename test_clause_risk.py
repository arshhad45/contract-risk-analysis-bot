from risk_engine.clause_risk import assess_clause_risk
from nlp.intent import detect_intent

clauses = [
    "The Company may terminate this agreement at its sole discretion.",
    "The Client shall pay INR 50,000 within 15 days.",
    "The Employee shall not disclose confidential information."
]

for clause in clauses:
    intent = detect_intent(clause)
    risks = assess_clause_risk(clause, intent)

    print("\nClause:", clause)
    print("Intent:", intent)
    print("Risks:", risks)
