import re

def clean_text(text: str) -> str:
    """
    Perform light text cleaning while preserving semantic meaning.
    """
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('\n', ' ').strip()
    return text
