# AI Document Summarization Tool

Overview

AI Document Summarizer is an analyst-focused, domain-agnostic document intelligence system that converts long, unstructured documents into structured, decision-ready summaries.

The system is designed to simulate LLM-style summarization workflows using explainable, heuristic-based NLP techniques, while maintaining a modular architecture that can be extended to Large Language Models (LLMs) in the future.

Rather than producing generic summaries, the tool structures output the way analysts consume information:

## Key Insights
- Metrics & Signals
- Risks / Concerns
- Recommended Actions

 
## Problem Statement
Analysts, consultants, and decision-makers frequently work with:
- economic outlook reports
- industry and market analysis
- policy and strategy documents
- resumes and screening documents

Manually extracting actionable information from such documents is time-consuming and inconsistent.

This project addresses that challenge by building a document intelligence pipeline that:
- preprocesses noisy real-world text
- filters irrelevant or boilerplate content
- surfaces analyst-relevant signals
- avoids hallucinating information not present in the source

## Key Features

* 📑 Multi-format document ingestion (PDF, TXT)
* 🧹 Content-aware preprocessing to clean noisy extracted text
* 🧩 Chunking strategy for large documents
* 🧠 Sentence-level classification into:
   - Insights
   - Metrics & Signals
   - Risks / Concerns
   - Recommended Actions
* 🧪 Heuristic filtering to remove:
   - citations
   - references
   - instructional or boilerplate text
* 📊 Analyst-style structured summaries
* 🔌 LLM-ready modular architecture

---

## Supported Document Types
The system is domain-agnostic, meaning it can process different document types, while keeping the output persona consistent (analyst / decision-maker).

Best suited for:
- Economic outlook reports (OECD, World Bank)
- Industry and market research reports
- Policy and strategy documents
- Consulting-style analytical reports
- Resumes (for analytical screening, not creative rewriting)

---

## Project Structure

AI-doc-summarizer/
│
├── data/
│   └── sample_docs/        # Sample documents (ignored in Git)
│
├── src/
│   ├── loader.py           # Document loading & preprocessing
│   ├── preprocess.py       # Text cleaning utilities
│   ├── chunker.py          # Chunking logic
│   ├── summarizer.py       # Insight extraction & classification
│   ├── evaluator.py        # Output validation
│   ├── doc_classifier.py   # Document type detection
│   ├── main.py             # Pipeline orchestration
│   └── __init__.py
│
├── requirements.txt
├── .gitignore
└── README.md


---

## Pipeline Overview

1. Document Loading
- Loads PDF or TXT files
- Applies basic content-aware skipping where possible

2.Preprocessing
- Cleans extracted text
- Removes excessive noise and formatting artifacts

3.Chunking
- Splits long documents into manageable chunks
- Enables scalable processing

4.Summarization & Classification
- Uses heuristic NLP rules to classify sentences into analyst-relevant  categories

5.Final Briefing Generation
- Aggregates chunk-level outputs
- Produces a structured executive briefing

---

## Example Output

DOCUMENT TYPE DETECTED: BUSINESS_REPORT

EXECUTIVE BRIEFING

KEY INSIGHTS:
- Productivity improvements could benefit downstream manufacturing sectors
- Structural reforms may improve capital and labor allocation
- The global economy remains resilient but faces underlying fragilities

METRICS & SIGNALS:
- Global GDP growth is projected to slow in the coming years
- Trade barriers and inflation pose downside risks

RISKS / CONCERNS:
- Rising macroeconomic uncertainty
- Exposure to policy and trade disruptions

RECOMMENDED ACTIONS:
- Strengthen productivity-enhancing reforms
- Support investment in high-impact sectors

---

## Installation & Usage

1. Clone the repository  
git clone https://github.com/anjali0614/AI-doc-summarizer.git
cd AI-doc-summarizer


2. Install dependencies  
pip install -r requirements.txt


3. Run the pipeline  
cd src
python main.py --file ../data/sample_docs/your_report.pdf



---

## Design Philosophy

✅ Analyst-first output, not generic summaries
✅ Explainable heuristics over black-box automation
✅ No hallucination of missing metrics or risks
✅ Clean version control (no raw data or generated files tracked)

---

## Limitations
Relies on PDF text extraction quality
Does not parse tables, charts, or scanned images
Heuristic rules may miss implicit or deeply contextual signals

These limitations are explicitly acknowledged and reflect real-world document intelligence trade-offs.


## Future Enhancements
- Integration with Large Language Models (LLMs) for abstractive      summarization
- Semantic classification using transformer-based models
- OCR support for scanned PDFs
- Layout-aware parsing for complex corporate filings
- API or web interface for interactive usage

---

## Tech Stack
- Python
- PyPDF2
- Heuristic NLP & rule-based text analysis
- Modular pipeline architecture

---

## Author

**Anjali Mina**  
GitHub: https://github.com/anjali0614  

---

## Final Note
This project focuses on realistic analyst workflows, prioritizing:
- clarity over hype
- correctness over hallucination
- explainability over black-box outputs

It is designed to demonstrate system thinking, data awareness, and decision-intelligence principles, rather than a single-model demo.
