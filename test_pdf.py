from utils.pdf_parser import extract_text_from_pdf
from utils.job_input import get_job_description
from utils.keyword_extractor import extract_keywords
from utils.match_score import calculate_match_score
from utils.ats_score import calculate_ats_score
from utils.suggestions import generate_suggestions

# 1. Extract resume text
resume_text = extract_text_from_pdf("data/resume.pdf")

# 2. Get job description
job_description = get_job_description()

# 3. Extract keywords
resume_keywords = extract_keywords(resume_text)
jd_keywords = extract_keywords(job_description)

# 4. Calculate match score
match_score, matched_skills, missing_skills = calculate_match_score(
    resume_keywords, jd_keywords
)

ats_score = calculate_ats_score(
    resume_text,
    jd_keywords,
    matched_skills
)

suggestions = generate_suggestions(
    missing_skills,
    matched_skills,
    resume_text
)


# 5. Print results
print("\n--- RESUME KEYWORDS ---\n")
print(resume_keywords)

print("\n--- JD KEYWORDS ---\n")
print(jd_keywords)

print("\n--- MATCH SCORE ---\n")
print("Match Score:", match_score)

print("\n--- MATCHED SKILLS ---\n")
print(matched_skills)

print("\n--- MISSING SKILLS ---\n")
print(missing_skills)

print("\n--- ATS SCORE ---\n")
print("ATS Score:", ats_score)

print("\n--- SUGGESTIONS ---\n")
for s in suggestions:
    print("-", s)