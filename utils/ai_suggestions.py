import requests
import os

# API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def generate_ai_suggestions(resume_text, job_description, missing_skills):
    try:
        prompt = f"""
        You are a resume expert.

        The candidate is missing these skills:
        {', '.join(missing_skills)}

        Give 3 short and practical resume improvement suggestions.
        """

        response = requests.post(
            API_URL,
            headers=HEADERS,
            json={"inputs": prompt},
            timeout=20
        )

        result = response.json()

        if isinstance(result, list):
            return result[0]["generated_text"]

        return (
            "Add more job-relevant projects, improve ATS keyword usage, "
            "and include missing technical skills like Git and FastAPI."
        )

    except Exception:
        # graceful fallback
        return (
            "Add more job-relevant projects, improve ATS keyword usage, "
            "and include missing technical skills like Git and FastAPI."
        )