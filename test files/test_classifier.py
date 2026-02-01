from nlp.classifier import classify_contract

sample_contracts = {
    "Employment": """
        This Employment Agreement is between employer and employee.
        The employee shall receive a monthly salary.
    """,

    "Service": """
        This Service Agreement defines the scope of work and deliverables
        to be provided by the service provider to the client.
    """,

    "Lease": """
        The landlord agrees to lease the premises to the tenant
        for a monthly rent of INR 20,000.
    """
}

for expected, text in sample_contracts.items():
    detected = classify_contract(text)
    print(f"Expected: {expected} | Detected: {detected}")
