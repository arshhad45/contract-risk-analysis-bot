from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def export_pdf(result, summary, filename="contract_report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    x = 40
    y = height - 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "Contract Risk Analysis Report")

    y -= 30
    c.setFont("Helvetica", 11)

    c.drawString(x, y, f"Contract Type: {summary['contract_type']}")
    y -= 20
    c.drawString(x, y, f"Overall Risk Level: {result['contract_risk']['label']}")
    y -= 20
    c.drawString(x, y, f"Total Clauses: {summary['total_clauses']}")
    y -= 20
    c.drawString(x, y, f"High Risk Clauses: {summary['high_risk_clauses']}")

    y -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y, "Clause Analysis")
    c.setFont("Helvetica", 10)

    for clause in result["clauses"]:
        if y < 80:
            c.showPage()
            c.setFont("Helvetica", 10)
            y = height - 40

        y -= 20
        c.drawString(x, y, f"Clause {clause['clause_id']}")

        y -= 15
        text = clause["text"][:120].replace("\n", " ")
        c.drawString(x, y, f"Text: {text}")

        y -= 15
        c.drawString(x, y, f"Intent: {clause['intent']}")

        if clause["unfavorable"]:
            y -= 15
            c.setFont("Helvetica-Bold", 10)
            c.drawString(x, y, "Unfavorable Clause")
            c.setFont("Helvetica", 10)

    c.save()
