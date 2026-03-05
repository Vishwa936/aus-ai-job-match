import streamlit as st

from src.preprocess import clean_text
from src.similarity import calculate_similarity
from src.keyword_extractor import extract_keywords, find_missing_keywords


st.title("AI Resume ↔ Job Match Analyzer")

st.write("Upload your resume and compare it with a job description.")


resume_text = st.text_area("Paste Resume Text")

job_description = st.text_area("Paste Job Description")


if st.button("Analyze Match"):

    if resume_text and job_description:

        resume_clean = clean_text(resume_text)
        job_clean = clean_text(job_description)

        text_similarity = calculate_similarity(resume_clean, job_clean) / 100

        resume_skills = extract_keywords(resume_clean)
        job_skills = extract_keywords(job_clean)

        matched_skills = resume_skills.intersection(job_skills)

        skill_ratio = len(matched_skills) / max(len(job_skills), 1)

        final_score = (0.7 * text_similarity) + (0.3 * skill_ratio)

        missing = find_missing_keywords(resume_clean, job_clean)

        st.subheader("Match Score")

        st.write(f"{round(final_score * 100, 2)} %")


        st.subheader("Matched Skills")

        for skill in sorted(matched_skills):
            st.write("•", skill)


        st.subheader("Missing Skills")

        for skill in sorted(missing):
            st.write("•", skill)

    else:
        st.warning("Please paste both resume and job description.")