def calculate_match_score(resume_keywords, jd_keywords):

    # convert to sets
    resume_set = set(resume_keywords)
    jd_set = set(jd_keywords)

    # matched skills
    matched_skills = list(
        resume_set.intersection(jd_set)
    )

    # missing skills
    missing_skills = list(
        jd_set - resume_set
    )

    # ✅ job-centric scoring
    if len(jd_set) == 0:
        match_score = 0

    else:
        match_score = (
            len(matched_skills) / len(jd_set)
        ) * 100

    return (
        round(match_score, 2),
        sorted(matched_skills),
        sorted(missing_skills)
    )