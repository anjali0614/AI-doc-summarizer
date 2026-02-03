def evaluate_summary(summary: str) -> dict:
    """
    Performs lightweight evaluation checks on the generated summary.
    """
    evaluation = {
        "length": len(summary),
        "has_executive_summary": "EXECUTIVE SUMMARY" in summary,
        "has_key_takeaways": "KEY TAKEAWAYS" in summary,
        "has_limitations": "LIMITATIONS" in summary
    }

    return evaluation
