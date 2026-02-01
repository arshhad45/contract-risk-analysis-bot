def classify_contract(text):
    text = text.lower()

    rules = {
        "Employment": [
            "employee", "employer", "salary", "termination", "notice period"
        ],
        "Service": [
            "services", "scope of work", "deliverables", "client"
        ],
        "Lease": [
            "rent", "premises", "landlord", "tenant"
        ],
        "Vendor": [
            "supplier", "purchase order", "goods"
        ],
        "Partnership": [
            "partner", "profit share", "capital contribution"
        ]
    }

    scores = {}

    for contract_type, keywords in rules.items():
        scores[contract_type] = sum(
            1 for kw in keywords if kw in text
        )

    return max(scores, key=scores.get)
