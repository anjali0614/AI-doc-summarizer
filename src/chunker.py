import tiktoken


def chunk_text(
    text: str,
    chunk_size: int = 800,
    overlap: int = 100
):
    """
    Split text into token-aware overlapping chunks.

    chunk_size: max tokens per chunk
    overlap: number of tokens to overlap between chunks
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    words = text.split()

    chunks = []
    current_chunk = []
    current_tokens = 0

    for word in words:
        token_count = len(encoding.encode(word))

        if current_tokens + token_count > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = current_chunk[-overlap:]
            current_tokens = len(
                encoding.encode(" ".join(current_chunk))
            )

        current_chunk.append(word)
        current_tokens += token_count

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
