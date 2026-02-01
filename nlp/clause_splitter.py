import re

def split_clauses(text):
    """
    Splits contract text into clauses based on numbering patterns.
    Returns a list of clause dictionaries.
    """

    # Non-capturing group is CRITICAL here
    pattern = r"\n\s*\d+(?:\.\d+)*[\.\)]\s+"

    raw_clauses = re.split(pattern, text)

    clauses = []
    clause_id = 1

    for clause in raw_clauses:
        if not clause:
            continue

        clause = clause.strip()
        if len(clause) < 40:
            continue

        clauses.append({
            "clause_id": clause_id,
            "text": clause
        })
        clause_id += 1

    return clauses
