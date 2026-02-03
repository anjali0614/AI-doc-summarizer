# AI Document Summarization Tool

An end-to-end AI-style document summarization system built using Python.  
This project demonstrates how large documents can be processed, chunked, summarized, and evaluated using a clean, modular pipeline similar to real-world LLM applications.

---

## Project Overview

The goal of this project is to design a scalable and maintainable document summarization pipeline.  
It processes long PDF or text documents and generates structured summaries while handling token limits through intelligent chunking.

The architecture is intentionally designed to resemble production-grade AI pipelines rather than a single-script solution.
The architecture mirrors real-world AI pipelines but uses rule-based and mock logic instead of live AI models.

---

## Key Features

- Document ingestion (PDF / text)
- Text cleaning and preprocessing
- Token-aware chunking for large documents
- Independent summarization of chunks
- Final structured summary generation
- Lightweight evaluation of summary quality
- Modular, extensible codebase
- Mock LLM-based summarization for cost-free experimentation  

---

## Architecture Overview

The pipeline follows a clear execution flow:

1. **Document Loader** (loader.py)
   Reads and extracts text from input files.

2. **Preprocessor** (preprocess.py)
   Cleans raw text by removing noise and normalizing content.

3. **Chunker** (chunker.py)
   Splits long documents into manageable, token-safe chunks.

4. **Summarization Layer**  (summarizer.py) 
   Each chunk is summarized independently using a mock LLM-style function.

5. **Summary Combiner**  (main.py)
   Individual summaries are merged into a final structured output.

6. **Evaluation Module** (evaluator.py) 
   Verifies completeness, structure, and basic quality metrics.

   Each component is independently testable and extendable.

---

## Tech Stack

- Python
- Virtual Environment (venv)
- Modular pipeline-based design
- Environment variable support
- Git & GitHub for version control

---

## Project Structure

AI-doc-summarizer/
│
├── src/
│ ├── loader/
│ ├── preprocessing/
│ ├── chunking/
│ ├── summarization/
│ ├── evaluation/
│ └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md



---

## How to Run Locally

1. Clone the repository  
git clone https://github.com/anjali0614/AI-doc-summarizer.git


2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate


3. Install dependencies  
pip install -r requirements.txt


4. Run the pipeline  
python -m src.main



---

## Output

- Structured document summary
- Key takeaways
- Summary length metrics
- Section presence validation

---

## Future Improvements

- Integration with real LLM APIs (OpenAI / Hugging Face)
- Improved evaluation metrics (ROUGE, semantic similarity)
- Web or API interface
- Support for more document formats

---

## Author

**Anjali Mina**  
GitHub: https://github.com/anjali0614  
