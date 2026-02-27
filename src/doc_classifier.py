def detect_document_type(text: str) -> str:
    """
    Detect document type using structural and semantic cues.
    """

    text_lower = text.lower()

    # Strong BUSINESS REPORT indicators
    business_markers = [
        "executive summary",
        "opportunity",
        "solution",
        "recommendation",
        "timeline",
        "costs",
        "conclusion",
        "references",
        "business report",
        "proposal"
    ]

    # Strong RESUME indicators
    resume_markers = [
        "education",
        "skills",
        "experience",
        "internship",
        "projects",
        "certifications",
        "linkedin",
        "github"
    ]

    business_score = sum(marker in text_lower for marker in business_markers)
    resume_score = sum(marker in text_lower for marker in resume_markers)

    # Structural dominance rule
    if business_score >= 2:
        return "business_report"

    if resume_score >= 3:
        return "resume"

    # Safe default for analyst role
    return "business_report"