def detect_intent(text):
    """
    Detects whether a clause expresses:
    - Obligation
    - Right
    - Prohibition
    """

    t = text.lower()

    if "shall not" in t or "must not" in t or "prohibited" in t:
        return "Prohibition"

    if "shall" in t or "must" in t:
        return "Obligation"

    if "may" in t or "is entitled to" in t:
        return "Right"

    return "Neutral"
