from nlp.intent import detect_intent

tests = {
    "The Client shall pay the invoice within 15 days.": "Obligation",
    "The Company may terminate this agreement at any time.": "Right",
    "The Employee shall not disclose confidential information.": "Prohibition",
    "This agreement governs the relationship between parties.": "Neutral"
}

for sentence, expected in tests.items():
    detected = detect_intent(sentence)
    print(f"Expected: {expected} | Detected: {detected}")
