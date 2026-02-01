def build_explanation_prompt(clause_text, intent, risks):
    risk_descriptions = []
    for r in risks:
        risk_descriptions.append(
            f"- Risk Type: {r['risk_type']}, Severity: {r['severity']}, Reason: {r['explanation']}"
        )

    risk_block = "\n".join(risk_descriptions) if risk_descriptions else "No significant risks detected."

    prompt = f"""
You are a contract explanation assistant for small business owners.

Rules:
- Do NOT give legal advice.
- Do NOT cite laws or regulations.
- Use simple business English.
- Explain in plain terms what the clause means and why it may be risky.

Clause Text:
\"\"\"{clause_text}\"\"\"

Clause Intent:
{intent}

Detected Risks:
{risk_block}

Tasks:
1. Explain what this clause means in simple language.
2. Explain why the identified risks matter to a small business.
3. If risky, suggest a safer, negotiation-friendly alternative clause.
"""
    return prompt


def generate_explanation(llm, clause_text, intent, risks):
    prompt = build_explanation_prompt(clause_text, intent, risks)
    return llm(prompt)
