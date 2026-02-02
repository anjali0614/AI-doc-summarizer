from src.loader import load_document

text = load_document("data/sample_docs/sample_report.pdf")
print(text[:500])
