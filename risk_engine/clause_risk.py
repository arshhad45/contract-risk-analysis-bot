import json

# Load rules once
with open("config/risk_rules.json", "r") as f:
    RISK_RULES = json.load(f)


def assess_clause_risk(clause_text, intent):
    """
    Assess risk of a clause based on keywords and intent.
    Returns a list of detected risks.
    """

    text = clause_text.lower()
    detected_risks = []

    for rule_name, rule in RISK_RULES.items():
        # Intent must match
        if rule["intent"] != intent:
            continue

        # Keyword match
        for kw in rule["keywords"]:
            if kw in text:
                detected_risks.append({
                    "risk_type": rule_name,
                    "severity": rule["severity"],
                    "explanation": rule["explanation"]
                })
                break

    return detected_risks
