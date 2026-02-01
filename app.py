import streamlit as st
import tempfile
import os

from pipeline import analyze_contract
from reporting.summary import generate_summary
from reporting.pdf_export import export_pdf


# ---------------- MOCK LLM ----------------
# Replace with GPT-4 / Claude only if allowed
def mock_llm(prompt):
    return "This clause has been explained in simple business language."


# ---------------- STREAMLIT CONFIG ----------------
st.set_page_config(
    page_title="Contract Risk Analysis Bot",
    layout="wide"
)

st.title("📄 Contract Risk Analysis Bot")


# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload Contract (PDF, DOCX, or TXT)",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    # ---- Save uploaded file temporarily (CRITICAL FIX) ----
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # Wrapper to match pipeline expectations (.path, .name, .read)
    class TempFileWrapper:
        def __init__(self, path, name):
            self.path = path
            self.name = name

        def read(self):
            with open(self.path, "rb") as f:
                return f.read()

    file_wrapper = TempFileWrapper(tmp_path, uploaded_file.name)

    # ---------------- ANALYSIS ----------------
    with st.spinner("Analyzing contract..."):
        result = analyze_contract(file_wrapper, mock_llm)
        summary = generate_summary(result)

    # Remove temp file (confidentiality)
    os.remove(tmp_path)

    st.success("Analysis completed")

    # ---------------- SUMMARY ----------------
    st.subheader("🔍 Contract Summary")
    st.json(summary)

    # ---------------- CLAUSE ANALYSIS ----------------
    st.subheader("📑 Clause-by-Clause Analysis")

    for clause in result["clauses"]:
        st.markdown("---")
        st.write(f"**Clause {clause['clause_id']}**")

        if clause["unfavorable"]:
            st.error("⚠ Unfavorable Clause")

        st.write(clause["text"])
        st.write("**Intent:**", clause["intent"])
        st.write("**Risks:**", clause["risks"])
        st.write("**Explanation:**")
        st.info(clause["explanation"])

    # ---------------- PDF EXPORT ----------------
    st.subheader("📄 Export Report")

    if st.button("📥 Generate PDF Report"):
        export_pdf(result, summary, filename="contract_report.pdf")

        with open("contract_report.pdf", "rb") as f:
            pdf_bytes = f.read()

        st.download_button(
            label="⬇ Download PDF Report",
            data=pdf_bytes,
            file_name="contract_report.pdf",
            mime="application/pdf"
        )
