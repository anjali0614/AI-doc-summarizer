def summarize_chunk(chunk: str) -> str:
    """
    Mock summarizer for a single chunk.
    Simulates LLM-style summarization.
    """
    sentences = chunk.split(".")
    bullets = sentences[:5]

    summary = "\n".join([f"- {s.strip()}" for s in bullets if s.strip()])
    return summary


def generate_final_summary(chunk_summaries: list) -> str:
    """
    Mock final summarization step.
    Combines chunk summaries into a structured output.
    """
    combined = "\n".join(chunk_summaries)

    final_summary = f"""
EXECUTIVE SUMMARY:
This document was automatically summarized using a mock LLM pipeline to extract key insights efficiently.

KEY TAKEAWAYS:
{combined}

LIMITATIONS:
- This is a mock summarization layer.
- Output quality depends on input structure.
- Can be replaced with live LLM APIs when enabled.
"""
    return final_summary


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
