from ingestion.loader import extract_text
from preprocessing.language import detect_language
from preprocessing.normalizer import normalize_to_english
from nlp.classifier import classify_contract
from nlp.clause_splitter import split_clauses
from nlp.ner import extract_entities
from nlp.intent import detect_intent
from risk_engine.clause_risk import assess_clause_risk
from risk_engine.contract_risk import calculate_contract_risk
from llm.reasoner import generate_explanation
from audit.logger import log_audit   # ✅ audit trail


def analyze_contract(file, llm):
    """
    Full contract analysis pipeline.
    Returns structured contract analysis.
    """

    # 1. Extract raw text
    raw_text = extract_text(file)

    # 2. Audit logging (hash only, no storage)
    log_audit(raw_text)

    # 3. Detect language
    language = detect_language(raw_text)

    # 4. Normalize text (Hindi → English internally)
    normalized_text = normalize_to_english(raw_text, language, llm)

    # 5. Classify contract type
    contract_type = classify_contract(normalized_text)

    # 6. Split into clauses
    clauses = split_clauses(normalized_text)

    enriched_clauses = []

    # 7. Clause-level analysis
    for clause in clauses:
        text = clause["text"]

        intent = detect_intent(text)
        entities = extract_entities(text)
        risks = assess_clause_risk(text, intent)

        # ✅ UNFAVORABLE CLAUSE FLAG (MANDATORY)
        is_unfavorable = any(
            r["severity"] == "High" for r in risks
        )

        explanation = generate_explanation(
            llm,
            text,
            intent,
            risks
        )

        enriched_clauses.append({
            "clause_id": clause["clause_id"],
            "text": text,
            "intent": intent,
            "entities": entities,
            "risks": risks,
            "unfavorable": is_unfavorable,   # ✅ added
            "explanation": explanation
        })

    # 8. Contract-level risk scoring
    contract_risk = calculate_contract_risk(enriched_clauses)

    # 9. Final structured output
    return {
        "contract_type": contract_type,
        "language": language,
        "contract_risk": contract_risk,
        "clauses": enriched_clauses
    }
