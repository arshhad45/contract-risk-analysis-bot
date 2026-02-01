def generate_summary(result):
    total_clauses = len(result["clauses"])
    high_risk = sum(
        1 for c in result["clauses"]
        for r in c["risks"] if r["severity"] == "High"
    )

    return {
        "contract_type": result["contract_type"],
        "overall_risk": result["contract_risk"]["label"],
        "total_clauses": total_clauses,
        "high_risk_clauses": high_risk,
        "key_message": (
            "Review high-risk clauses before signing."
            if high_risk > 0 else
            "No major risks detected."
        )
    }
