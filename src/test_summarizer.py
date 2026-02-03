from src.loader import load_document
from src.preprocess import clean_text
from src.chunker import chunk_text
from src.summarizer import summarize_chunk, generate_final_summary

text = load_document("data/sample_docs/sample_report.pdf")
cleaned = clean_text(text)
chunks = chunk_text(cleaned)

chunk_summaries = []
for i, chunk in enumerate(chunks):
    print(f"\n--- Summarizing chunk {i+1}/{len(chunks)} ---")
    summary = summarize_chunk(chunk)
    print(summary)
    chunk_summaries.append(summary)

final_summary = generate_final_summary(chunk_summaries)

print("\n===== FINAL SUMMARY =====\n")
print(final_summary)
