# Project Description

Contract Analysis & Risk Assessment Bot

## Overview

The Contract Analysis & Risk Assessment Bot is a GenAI-powered legal assistant designed to help small and medium business (SME) owners understand complex contracts, identify potential risks, and make informed decisions before signing agreements.

Many SMEs lack access to affordable legal review and often sign contracts without fully understanding unfavorable terms, hidden liabilities, or restrictive clauses. This system addresses that gap by transforming dense legal language into clear, actionable insights using Natural Language Processing (NLP) and controlled Generative AI reasoning.

## Problem It Solves

Business contracts such as service agreements, employment contracts, vendor agreements, and partnership deeds often contain:

One-sided termination rights

Heavy penalty clauses

Intellectual property transfers

Non-compete restrictions

Auto-renewal lock-ins

Jurisdiction limitations

These clauses can expose SMEs to financial, operational, and legal risks.

Manual legal review is:

Expensive

Time-consuming

Not always accessible to small businesses

This project provides an automated, explainable, and affordable first-level contract risk analysis system.

What the System Does

The platform performs end-to-end contract intelligence analysis through a structured pipeline:

1. Document Ingestion

Supports multiple contract formats:

PDF (text-based)

DOC / DOCX

Plain text (.txt)

The system extracts and normalizes text for downstream analysis.

2. Multilingual Processing

Detects contract language (English / Hindi)

Normalizes Hindi text into English internally for NLP processing

Outputs explanations in simple business English

3. Contract Type Classification

Automatically identifies contract categories such as:

Service agreements

Employment contracts

Vendor agreements

Lease agreements

Partnership deeds

4. Clause & Sub-Clause Extraction

Contracts are segmented into structured clauses to enable granular risk analysis instead of treating the document as a single block of text.

5. Named Entity Recognition (NER)

Extracts key legal and business entities, including:

Parties / Organizations

Financial amounts

Dates & durations

Jurisdiction locations

Obligations & deliverables

6. Clause Intent Detection

Each clause is classified into:

Obligation

Right

Prohibition

This helps determine who is responsible, empowered, or restricted.

7. Risk Detection & Compliance Heuristics

The system identifies high-risk and unfavorable legal constructs such as:

Penalty clauses

Indemnity liabilities

Unilateral termination rights

Auto-renewal & lock-in periods

Non-compete restrictions

Intellectual property transfers

Arbitration & jurisdiction constraints

Each clause is assigned a risk severity level:

Low

Medium

High

8. Contract-Level Risk Scoring

Clause scores are aggregated to compute a composite contract risk rating, enabling quick executive assessment.

9. Plain-Language GenAI Explanations

Using controlled LLM reasoning, the system generates:

Clause-by-clause explanations

Risk impact summaries

Business implications

Negotiation-friendly alternatives

All explanations are delivered in simple, non-legal business language.

10. Unfavorable Clause Highlighting

Clauses deemed high risk are visually flagged to draw immediate attention for review or renegotiation.

11. Summary Reports & PDF Export

The system generates structured analysis reports including:

Contract type

Overall risk score

Clause risk distribution

High-risk clause count

Reports can be exported as professional PDFs for legal consultation or management review.

12. Confidentiality & Audit Logging

To maintain document privacy:

Contracts are processed locally

Only hashed audit logs are stored

No raw contract text is retained

This ensures secure handling of sensitive agreements.

Technology Stack

Frontend/UI: Streamlit

Backend: Python

NLP Processing: spaCy, rule-based pipelines

Generative Reasoning: GPT-class LLM (explanation only)

Document Parsing: pdfplumber, python-docx

Reporting: ReportLab (PDF generation)

Storage: Local files + JSON audit logs

Responsible AI & Compliance

This system:

Does not provide legal advice

Does not cite statutes or case law

Performs heuristic risk detection based on SME best practices

Uses LLMs only for controlled explanation generation

This ensures ethical and competition-compliant deployment.

Impact

By simplifying contract comprehension and surfacing hidden risks, the platform enables SMEs to:

Avoid unfavorable agreements

Negotiate better terms

Reduce legal exposure

Make informed signing decisions

Conclusion

The Contract Analysis & Risk Assessment Bot bridges the gap between complex legal documentation and business understanding by combining NLP, explainable AI, and structured risk intelligence into a practical, accessible decision-support tool for small and medium enterprises.
