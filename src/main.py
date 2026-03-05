from preprocess import clean_text
from similarity import calculate_similarity
from keyword_extractor import extract_keywords, find_missing_keywords


if __name__ == "__main__":

    resume = """
    Python developer with experience in Django, REST APIs, PostgreSQL,
    machine learning, and data analysis.
    """

    job_description = """
    Looking for a Python developer with experience in Django, REST APIs,
    PostgreSQL, machine learning, Docker and AWS.
    """

    resume_clean = clean_text(resume)
    job_clean = clean_text(job_description)

    # TEXT SIMILARITY
    text_similarity = calculate_similarity(resume_clean, job_clean) / 100

    # SKILL EXTRACTION
    resume_skills = extract_keywords(resume_clean)
    job_skills = extract_keywords(job_clean)

    matched_skills = resume_skills.intersection(job_skills)

    skill_ratio = len(matched_skills) / len(job_skills)

    # FINAL SCORE
    final_score = (0.7 * text_similarity) + (0.3 * skill_ratio)

    missing = find_missing_keywords(resume_clean, job_clean)

    print(f"Match Score: {round(final_score*100,2)}%")

    print("\nMatched Skills:")
    for skill in matched_skills:
        print(f"- {skill}")

    print("\nMissing Keywords:")
    for skill in missing:
        print(f"- {skill}")