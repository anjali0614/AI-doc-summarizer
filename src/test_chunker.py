from src.loader import load_document
from src.preprocess import clean_text
from src.chunker import chunk_text

text = load_document("data/sample_docs/sample_report.pdf")
cleaned = clean_text(text)

chunks = chunk_text(cleaned)

print(f"Total chunks: {len(chunks)}")
print("\n--- FIRST CHUNK ---\n")
print(chunks[0][:500])
