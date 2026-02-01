from risk_engine.contract_risk import calculate_contract_risk

clauses_with_risks = [
    {
        "text": "The Company may terminate this agreement at its sole discretion.",
        "risks": [
            {"severity": "High"}
        ]
    },
    {
        "text": "The Client shall pay INR 50,000 within 15 days.",
        "risks": [
            {"severity": "Medium"}
        ]
    },
    {
        "text": "The Employee shall not disclose confidential information.",
        "risks": [
            {"severity": "Low"}
        ]
    }
]

result = calculate_contract_risk(clauses_with_risks)

print("Contract Risk Result:")
print(result)
