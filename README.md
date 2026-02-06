## Contract Analysis & Risk Assessment Bot

A GenAI-powered legal assistant that helps small and medium businesses understand complex contracts, identify risks, and receive plain-language explanations before signing agreements.

## Overview

Small and medium enterprises (SMEs) often sign contracts without fully understanding legal language, hidden liabilities, or unfavorable clauses. Legal consultation is expensive and not always accessible.

The Contract Analysis & Risk Assessment Bot automates contract review by combining NLP and controlled Generative AI to:

Analyze contracts clause by clause

Detect legal and financial risks

Explain clauses in simple business language

Suggest safer negotiation alternatives

Generate downloadable risk reports

## Key Features
## Multi-Format Contract Upload

Supports:

PDF (text-based)

DOC / DOCX

Plain text (.txt)

# Multilingual Processing

Detects English and Hindi contracts

Normalizes Hindi → English internally

Outputs explanations in simple business English

## Contract Type Classification

Automatically identifies contract types such as:

Service Agreements

Employment Contracts

Vendor Agreements

Lease Agreements

Partnership Deeds

## Clause Extraction

Splits contracts into structured clauses for granular analysis.

## Named Entity Recognition

Extracts key entities:

Parties / Organizations

Financial amounts

Dates & durations

Jurisdiction locations

Deliverables & obligations

⚖ Clause Intent Detection

Classifies clauses into:

Obligation

Right

Prohibition

## Risk Detection Engine

Identifies unfavorable clauses including:

Penalty clauses

Indemnity liabilities

Unilateral termination

Auto-renewal lock-ins

Non-compete restrictions

IP ownership transfers

Arbitration & jurisdiction terms

Each clause is assigned:

Low Risk

Medium Risk

High Risk

## Contract Risk Scoring

Generates an overall contract risk rating based on clause-level severity.

## Plain-Language AI Explanations

Uses controlled LLM reasoning to:

Explain clauses in simple terms

Highlight business impact

Suggest safer alternatives

## The system does not provide legal advice.

## PDF Report Export

Generates downloadable reports containing:

Contract summary

Risk distribution

Clause explanations

Unfavorable clause highlights

## Confidentiality & Audit Logs

Contracts processed locally

No raw text stored

Hash-based audit logging

# Architecture Pipeline
Upload Contract
      ↓
Text Extraction
      ↓
Language Detection
      ↓
Normalization
      ↓
Contract Classification
      ↓
Clause Splitting
      ↓
NER + Intent Detection
      ↓
Risk Engine
      ↓
LLM Explanation
      ↓
Risk Scoring
      ↓
PDF Report

- Tech Stack
Layer	Technology
UI	Streamlit
Backend	Python
NLP	spaCy
GenAI	GPT-class LLM (explanations only)
Document Parsing	pdfplumber, python-docx
Reporting	ReportLab
Storage	Local + JSON audit logs

# Installation (Local Setup)
# Clone repo
git clone https://github.com/your-username/contract-risk-analysis-bot.git
cd contract-risk-analysis-bot

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py

# Deployment

This project is deployed using Streamlit Community Cloud.

Steps:

Push repo to GitHub

Add requirements.txt

Deploy via Streamlit Cloud dashboard

Set app.py as entry point

# Sample Use Case

Upload a service agreement containing:

“The Company may terminate this agreement at its sole discretion.”

The system will:

Flag it as High Risk

Explain why it is unfavorable

Suggest a safer termination clause

⚠ Responsible AI Disclaimer

This tool:

Does not provide legal advice

Does not cite statutes or case law

Performs heuristic risk detection based on SME best practices

Uses LLMs only for controlled explanation generation

# Impact

Helps SMEs:

Understand contracts before signing

Detect hidden risks

Negotiate better terms

Reduce legal exposure
