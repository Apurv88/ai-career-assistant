def clean_skill_names(skills):
    mapping = {
        "machine": "machine learning",
        "learning": "machine learning",
        "data": "data analysis"
    }

    cleaned = []
    for skill in skills:
        if skill in mapping:
            cleaned.append(mapping[skill])
        else:
            cleaned.append(skill)

    # remove duplicates
    return list(set(cleaned))


def sort_skills(skills):
    return sorted(skills)

def generate_explanation(match_score, ats_score):
    if match_score > 70:
        match_msg = "Your resume is highly aligned with the job."
    elif match_score > 40:
        match_msg = "Your resume is moderately aligned with the job."
    else:
        match_msg = "Your resume has low alignment with the job."

    if ats_score > 75:
        ats_msg = "Your resume is well optimized for ATS systems."
    else:
        ats_msg = "Your resume can be improved for better ATS performance."

    return match_msg + " " + ats_msg