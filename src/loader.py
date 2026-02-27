from PyPDF2 import PdfReader


def load_document(file_path: str) -> str:
    """
    Load text from a PDF or TXT file.
    Skips front-matter and legal scope sections in corporate reports
    by starting extraction only after business narrative begins.
    """

    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        text = ""
        start_collecting = False

        business_start_markers = [
            "our strategy",
            "business model",
            "performance highlights",
            "chair’s statement",
            "chairman's statement",
            "ceo review",
            "chief executive",
            "strategic priorities",
            "overview"
        ]

        for page in reader.pages:
            extracted = page.extract_text()
            if not extracted:
                continue

            lower_text = extracted.lower()

            # 🔑 Detect start of real business content
            if not start_collecting:
                if any(marker in lower_text for marker in business_start_markers):
                    start_collecting = True
                else:
                    continue  # skip legal / index pages

            # Collect only meaningful pages
            text += extracted + "\n"

        return text

    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    else:
        raise ValueError("Unsupported file format")
