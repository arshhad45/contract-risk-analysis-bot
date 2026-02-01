SEVERITY_SCORES = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

def calculate_contract_risk(clauses_with_risks):
    """
    clauses_with_risks: list of clauses, each containing a 'risks' list
    Returns composite score and risk label.
    """

    total_score = 0
    risk_count = 0

    for clause in clauses_with_risks:
        for risk in clause.get("risks", []):
            total_score += SEVERITY_SCORES.get(risk["severity"], 0)
            risk_count += 1

    if risk_count == 0:
        return {
            "score": 0,
            "label": "Low",
            "message": "No significant risks detected."
        }

    average_score = total_score / risk_count

    if average_score >= 2.5:
        label = "High"
    elif average_score >= 1.5:
        label = "Medium"
    else:
        label = "Low"

    return {
        "score": round(average_score, 2),
        "label": label,
        "message": f"Overall contract risk assessed as {label}."
    }
