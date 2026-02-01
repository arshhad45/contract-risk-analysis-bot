def extract_text(file):
    # PDF
    if file.name.endswith(".pdf"):
        import pdfplumber
        with pdfplumber.open(file.path) as pdf:
            return "\n".join(
                page.extract_text() or "" for page in pdf.pages
            )

    # DOCX
    if file.name.endswith(".docx"):
        from docx import Document
        doc = Document(file.path)
        return "\n".join(p.text for p in doc.paragraphs)

    # TXT
    return file.read().decode("utf-8", errors="ignore")
