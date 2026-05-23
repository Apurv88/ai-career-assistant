from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import shutil
import os

# 🔹 Utils imports
from utils.real_job_api import fetch_real_jobs
from utils.pdf_parser import extract_text_from_pdf
from utils.keyword_extractor import extract_keywords
from utils.match_score import calculate_match_score
from utils.ats_score import calculate_ats_score
from utils.suggestions import generate_suggestions
from utils.postprocess import clean_skill_names, sort_skills, generate_explanation
from utils.ai_suggestions import generate_ai_suggestions
from utils.job_agent import (
    search_jobs,
    recommend_jobs
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "AI Career Assistant API Running"}


@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form("")
):
    try:
        # 🔹 1. Validate file
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files allowed")

        # 🔹 2. Save file
        file_path = f"data/{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 🔹 3. Extract text
        resume_text = extract_text_from_pdf(file_path)

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Unable to extract text from PDF")

        # 🔹 4. Extract keywords
        resume_keywords = extract_keywords(resume_text)
        jd_keywords = extract_keywords(job_description)

        # 🔹 5. Match score
        match_score, matched_skills, missing_skills = calculate_match_score(
            resume_keywords, jd_keywords
        )

        # 🔹 6. ATS score
        ats_score = calculate_ats_score(
            resume_text,
            jd_keywords,
            matched_skills
        )

        # 🔹 7. Suggestions
        suggestions = generate_suggestions(
            missing_skills,
            matched_skills,
            resume_text
        )

        # 🔹 8. Post-processing (🔥 FIXED PART)
        matched_skills = clean_skill_names(matched_skills)
        missing_skills = clean_skill_names(missing_skills)

        missing_skills = [s for s in missing_skills if s not in matched_skills]

        matched_skills = sort_skills(matched_skills)
        missing_skills = sort_skills(missing_skills)

        suggestions = generate_suggestions(
        missing_skills,
        matched_skills,
        resume_text
        )
        explanation = generate_explanation(match_score, ats_score)
        ai_suggestions = generate_ai_suggestions(
    resume_text,
    job_description,
    missing_skills
                  )

        # 🔹 9. Cleanup file
        if os.path.exists(file_path):
            os.remove(file_path)

        # 🔹 10. Final response
        return {
            "match_score": match_score,
            "ats_score": ats_score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "suggestions": ai_suggestions,
            "explanation": explanation
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/jobs")
def get_jobs(role: str):

    results = search_jobs(role)

    if not results:
        return {
            "message": "No jobs found"
        }

    return results

@app.post("/recommend-jobs")
async def recommend_jobs_api(
    file: UploadFile = File(...)
):

    try:

        # save uploaded file
        file_path = f"data/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # extract resume text
        resume_text = extract_text_from_pdf(file_path)

        # extract skills
        resume_keywords = extract_keywords(
            resume_text
        )

        # get recommendations
        recommendations = recommend_jobs(
            resume_keywords
        )

        # cleanup
        os.remove(file_path)

        return recommendations

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    


@app.get("/real-jobs")
def real_jobs(role: str):

    jobs = fetch_real_jobs(role)

    return jobs    