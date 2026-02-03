from src.loader import load_document
from src.preprocess import clean_text
from src.chunker import chunk_text
from src.summarizer import summarize_chunk, generate_final_summary
from src.evaluator import evaluate_summary


def run_pipeline(file_path: str):
    """
    Orchestrates the full document summarization pipeline.
    """
    # Step 1: Load
    raw_text = load_document(file_path)

    # Step 2: Preprocess
    cleaned_text = clean_text(raw_text)

    # Step 3: Chunk
    chunks = chunk_text(cleaned_text)

    # Step 4: Summarize each chunk
    chunk_summaries = []
    for chunk in chunks:
        summary = summarize_chunk(chunk)
        chunk_summaries.append(summary)

    # Step 5: Generate final summary
    final_summary = generate_final_summary(chunk_summaries)

    # Step 6: Evaluate output
    evaluation = evaluate_summary(final_summary)

    return final_summary, evaluation


if __name__ == "__main__":
    file_path = "data/sample_docs/sample_report.pdf"

    summary, evaluation = run_pipeline(file_path)

    print("\n===== FINAL SUMMARY =====\n")
    print(summary)

    print("\n===== EVALUATION =====\n")
    print(evaluation)
