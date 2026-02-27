import re


def summarize_chunk(chunk: str, method: str = "analyst") -> dict:

    instructional_phrases = [
        "should include",
        "important to include",
        "this section",
        "when possible",
        "create a chart",
        "the purpose of this report",
        "this sample",
        "the following example"
    ]

    reference_markers = [
    "references",
    "review",
    "journal",
    "volume",
    "issue",
    "pp",
    "no.",
    "contreras"
]

    sentences = [s.strip() for s in chunk.split(".") if s.strip()]

    insights = []
    metrics = []
    risks = []
    actions = []

    for s in sentences:
        s_lower = s.lower()

        # bibliography / reference titles
        if any(r in s_lower for r in reference_markers):
            continue

        # very short / broken lines
        if len(s_lower) < 15:
            continue

        # instructional / academic lines
        if any(p in s_lower for p in instructional_phrases):
            continue

        # references / URLs
        if "http" in s_lower or "www" in s_lower:
            continue

        # citations like (2012)
        if re.search(r"\(\d{4}\)", s_lower):
            continue

        # 📊 Metrics
        if any(k in s_lower for k in ["increase", "decrease", "growth", "decline"]):
            metrics.append(s)

        # ⚠️ Risks
        elif any(k in s_lower for k in ["risk", "issue", "challenge", "concern"]):
            risks.append(s)

        # 🎯 Actions
        elif any(k in s_lower for k in [
            "will", "plan", "aim", "goal", "strategy",
            "phase", "initiative", "propose", "focus"
        ]):
            actions.append(s)

        # 💡 Insights
        else:
            insights.append(s)

    return {
        "insights": insights[:3],
        "metrics": metrics[:2],
        "risks": risks[:2],
        "actions": actions[:2]
    }


def generate_final_summary(chunk_outputs: list, doc_type: str) -> str:
    """
    Combine analyst insights from all chunks into a briefing-style summary.
    """

    insights, metrics, risks, actions = [], [], [], []

    for chunk in chunk_outputs:
        insights.extend(chunk["insights"])
        metrics.extend(chunk["metrics"])
        risks.extend(chunk["risks"])
        actions.extend(chunk["actions"])

    final_summary = f"""
DOCUMENT TYPE DETECTED: {doc_type.upper()}

EXECUTIVE BRIEFING

KEY INSIGHTS:
- """ + "\n- ".join(insights[:5]) + """

METRICS & SIGNALS:
- """ + "\n- ".join(metrics[:4]) + """

RISKS / CONCERNS:
- """ + "\n- ".join(risks[:4]) + """

RECOMMENDED ACTIONS:
- """ + "\n- ".join(actions[:4]) + """
"""

    return final_summary.strip() 


# import os
# from dotenv import load_dotenv
# from openai import OpenAI

# # load environment variables FIRST
# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# def summarize_chunk(chunk: str) -> str:
#     """
#     Generate a concise summary for a single text chunk.
#     """
#     prompt = f"""
#     Summarize the following text into 5-7 concise bullet points.
#     Focus on key facts, insights, and important details.
    
#     TEXT:
#     {chunk}
#     """

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.3
#     )

#     return response.choices[0].message.content


# def generate_final_summary(chunk_summaries: list) -> str:
#     """
#     Combine chunk-level summaries into a structured final summary.
#     """
#     combined_summaries = "\n".join(chunk_summaries)

#     prompt = f"""
#     Using the summaries below, generate:
#     1. An executive summary (short paragraph)
#     2. Key takeaways (bullet points)
#     3. Potential risks or limitations (bullet points)

#     SUMMARIES:
#     {combined_summaries}
#     """

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.3
#     )

#     return response.choices[0].message.content
