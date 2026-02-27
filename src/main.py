import argparse

from loader import load_document
from preprocess import clean_text
from chunker import chunk_text
from summarizer import summarize_chunk, generate_final_summary
from evaluator import evaluate_summary
from doc_classifier import detect_document_type


def run_pipeline(file_path: str, chunk_size: int, method: str):
    """
    Orchestrates the full document summarization pipeline.
    """

    # Step 1: Load document
    raw_text = load_document(file_path)

    # Step 2: Preprocess text
    cleaned_text = clean_text(raw_text)

    #Step 3: Classify the document type
    doc_type = detect_document_type(cleaned_text)

    # Step 4: Chunk document
    chunks = chunk_text(cleaned_text, chunk_size=chunk_size)

    # Step 5: Summarize each chunk
    chunk_outputs = []
    for chunk in chunks:
     output = summarize_chunk(chunk)
    chunk_outputs.append(output)

    # Step 6: Generate final summary
    final_summary = generate_final_summary(chunk_outputs, doc_type)

    # Step 7: Evaluate summary
    evaluation = evaluate_summary(final_summary)

    return final_summary, evaluation


def main():
    parser = argparse.ArgumentParser(description="AI Document Summarization System")

    parser.add_argument(
        "--file",
        required=True,
        help="Path to input document (PDF / TXT)"
    )

    parser.add_argument(
        "--chunk_size",
        type=int,
        default=500,
        help="Number of words per chunk"
    )

    parser.add_argument(
        "--method",
        choices=["extractive", "abstractive", "hybrid"],
        default="abstractive",
        help="Summarization strategy"
    )

    args = parser.parse_args()

    summary, evaluation = run_pipeline(
        file_path=args.file,
        chunk_size=args.chunk_size,
        method=args.method
    )

    print("\n===== FINAL SUMMARY =====\n")
    print(summary)

    print("\n===== EVALUATION =====\n")
    print(evaluation)


if __name__ == "__main__":
    main()
