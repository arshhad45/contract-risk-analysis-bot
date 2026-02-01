from llm.reasoner import generate_explanation

# Mock LLM (simulates GPT response)
def mock_llm(prompt):
    return """
Explanation:
This clause allows the company to end the contract whenever it wants.

Why it matters:
This puts the other party at risk because they may lose business suddenly.

Suggested Alternative:
Either party may terminate the agreement with 30 days written notice and valid reason.
"""

clause = "The Company may terminate this agreement at its sole discretion."
intent = "Right"
risks = [
    {
        "risk_type": "unilateral_termination",
        "severity": "High",
        "explanation": "One party can end the contract without protection for the other party."
    }
]

result = generate_explanation(
    mock_llm,
    clause,
    intent,
    risks
)

print(result)
