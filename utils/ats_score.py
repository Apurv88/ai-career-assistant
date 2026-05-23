def calculate_ats_score(resume_text, jd_keywords, matched_keywords):
    resume_lower = resume_text.lower()
    total_score = 0

    # 🔹 1. Keyword Match (40%)
    if len(jd_keywords) > 0:
        keyword_score = (len(matched_keywords) / len(jd_keywords)) * 40
    else:
        keyword_score = 0

    # 🔹 2. Section Presence (20%)
    sections = ["skills", "education", "experience", "project"]
    section_score = 0

    for section in sections:
        if section in resume_lower:
            section_score += 5  # 4 sections × 5 = 20

    # 🔹 3. Skill Density (20%)
    words = resume_lower.split()
    total_words = len(words)

    skill_count = 0
    for skill in jd_keywords:
        skill_count += resume_lower.count(skill)

    if total_words > 0:
        density = skill_count / total_words
        density_score = min(density * 200, 20)  # scale to max 20
    else:
        density_score = 0

    # 🔹 4. Formatting & Readability (20%)

    # Length check
    if 300 <= total_words <= 900:
        length_score = 10
    else:
        length_score = 5

    # Structure check
    if "\n" in resume_text:
        structure_score = 10
    else:
        structure_score = 5

    formatting_score = length_score + structure_score

    # 🔹 Final Score
    total_score = keyword_score + section_score + density_score + formatting_score

    return round(total_score, 2)