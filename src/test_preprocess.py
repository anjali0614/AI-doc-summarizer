from src.loader import load_document
from src.preprocess import clean_text

raw_text = load_document("data/sample_docs/sample_report.pdf")
cleaned = clean_text(raw_text)

print(cleaned[:500])
