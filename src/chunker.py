import tiktoken

def chunk_text(text: str, max_tokens: int = 800, overlap: int = 100):
    """
    Split text into token-aware overlapping chunks.
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    words = text.split()

    chunks = []
    current_chunk = []
    current_tokens = 0

    for word in words:
        token_count = len(encoding.encode(word))

        if current_tokens + token_count > max_tokens:
            chunks.append(" ".join(current_chunk))
            # overlap to preserve context
            current_chunk = current_chunk[-overlap:]
            current_tokens = len(encoding.encode(" ".join(current_chunk)))

        current_chunk.append(word)
        current_tokens += token_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
