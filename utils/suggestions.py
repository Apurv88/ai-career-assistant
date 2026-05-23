def generate_suggestions(missing_skills, matched_skills, resume_text):
    suggestions = []

    # 🔹 Missing skills (improved)
    if missing_skills:
        suggestions.append(
            "Consider adding these skills with practical examples: " + ", ".join(missing_skills)
        )

    # 🔹 Match quality
    if len(matched_skills) < 4:
        suggestions.append(
            "Your resume is not strongly aligned with the job. Tailor it specifically for this role."
        )

    resume_lower = resume_text.lower()

    # 🔹 Sections
    if "skills" not in resume_lower:
        suggestions.append("Add a dedicated 'Skills' section with technical tools.")

    if "project" not in resume_lower:
        suggestions.append("Include 1-2 strong projects related to the job role.")

    if "experience" not in resume_lower:
        suggestions.append("Add internships or practical experience.")

    # 🔹 Strong improvement tip
    suggestions.append(
        "Use keywords from the job description naturally in your resume (especially in projects and experience)."
    )

    return suggestions