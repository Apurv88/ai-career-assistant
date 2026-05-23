from utils.match_score import calculate_match_score
from utils.real_job_api import fetch_real_jobs


# ✅ Search jobs from Adzuna API
def search_jobs(role):

    return fetch_real_jobs(role)


# ✅ Recommend jobs based on resume skills
def recommend_jobs(resume_keywords):

    # convert resume skills into search query
    role = "python developer"

    if "machine learning" in resume_keywords:
        role = "machine learning engineer"

    elif "data science" in resume_keywords:
        role = "data scientist"

    elif "fastapi" in resume_keywords:
        role = "backend developer"

    # fetch real jobs
    jobs = fetch_real_jobs(role)

    recommendations = []

    for job in jobs:

        # dummy scoring
        score = 75

        if "python" in resume_keywords:
            score += 10

        recommendations.append({

            "title": job.get("title"),

            "company": job.get("company"),

            "location": job.get("location"),

            "match_score": min(score, 100),

            "redirect_url": job.get("redirect_url")

        })

    return recommendations