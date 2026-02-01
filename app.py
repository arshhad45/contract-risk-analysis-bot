import streamlit as st
import tempfile
import os

from pipeline import analyze_contract
from reporting.summary import generate_summary
from reporting.pdf_export import export_pdf


# ---------------- MOCK LLM ----------------
def mock_llm(prompt):
    return "This clause has been explained in simple business language."


# ---------------- STREAMLIT CONFIG ----------------
st.set_page_config(
    page_title="Contract Risk Analysis Bot",
    layout="wide"
)

st.title("📄 Contract Risk Analysis Bot")


# ---------------- CACHED ANALYSIS FUNCTION ----------------
@st.cache_data(show_spinner=False)
def run_analysis(file_bytes, file_name):
    """
    Runs contract analysis only once per uploaded file.
    Prevents infinite reruns and browser freeze.
    """
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    class TempFileWrapper:
        def __init__(self, path, name):
            self.path = path
            self.name = name

        def read(self):
            with open(self.path, "rb") as f:
                return f.read()

    wrapped_file = TempFileWrapper(tmp_path, file_name)
    result = analyze_contract(wrapped_file, mock_llm)

    os.remove(tmp_path)
    return result


# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload Contract (PDF, DOCX, or TXT)",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:

    # ---------- RUN ANALYSIS ONLY ONCE ----------
    if "analysis_result" not in st.session_state:
        with st.spinner("Analyzing contract..."):
            st.session_state.analysis_result = run_analysis(
                uploaded_file.getvalue(),
                uploaded_file.name
            )

    result = st.session_state.analysis_result
    summary = generate_summary(result)

    st.success("Analysis completed")

    # ---------------- SUMMARY ----------------
    st.subheader("🔍 Contract Summary")
    st.json(summary)

    # ---------------- CLAUSE ANALYSIS ----------------
    st.subheader("📑 Clause-by-Clause Analysis")

    for clause in result["clauses"]:
        st.markdown("---")
        st.write(f"**Clause {clause['clause_id']}**")

        if clause.get("unfavorable"):
            st.error("⚠ Unfavorable Clause")

        st.write(clause["text"])
        st.write("**Intent:**", clause["intent"])
        st.write("**Risks:**", clause["risks"])
        st.write("**Explanation:**")
        st.info(clause["explanation"])

    # ---------------- PDF EXPORT ----------------
    st.subheader("📄 Export Report")

    if "pdf_ready" not in st.session_state:
        st.session_state.pdf_ready = False

    if st.button("📥 Generate PDF Report"):
        export_pdf(result, summary, filename="contract_report.pdf")
        st.session_state.pdf_ready = True

    if st.session_state.pdf_ready:
        with open("contract_report.pdf", "rb") as f:
            st.download_button(
                label="⬇ Download PDF Report",
                data=f,
                file_name="contract_report.pdf",
                mime="application/pdf"
            )
