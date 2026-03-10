import streamlit as st

from src.preprocess import clean_text
from src.ai.skill_extractor_llm import extract_skills_both
from src.ai.suggestion_llm import generate_suggestions
from src.file_parser import extract_text_from_pdf, extract_text_from_docx


st.title("AI Resume ↔ Job Match Analyzer")

st.write("Upload your resume or paste it manually.")

# ---------- Resume Upload ----------
uploaded_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)", type=["pdf", "docx"]
)

resume_text = ""

if uploaded_file is not None:

    if uploaded_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_file)

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_text_from_docx(uploaded_file)

    st.success("Resume uploaded successfully!")

# ---------- Manual Resume Input ----------
resume_text_manual = st.text_area("Or paste resume text here")

if resume_text_manual:
    resume_text = resume_text_manual


# ---------- Job Description ----------
job_text = st.text_area("Paste Job Description")


# ---------- Analyze ----------
if st.button("Analyze Match"):

    if resume_text and job_text:

        with st.spinner("Analyzing resume..."):

            resume_clean = clean_text(resume_text)
            job_clean = clean_text(job_text)

            matched_skills, missing_skills = extract_skills_both(
                resume_clean, job_clean
            )

            total_skills = len(matched_skills) + len(missing_skills)

            score = len(matched_skills) / total_skills if total_skills else 0
            score_percent = round(score * 100, 2)

            suggestions = generate_suggestions(missing_skills) if missing_skills else []

        # ---------- OUTPUT ----------
        st.subheader(f"Match Score: {score_percent}%")

        st.subheader("Matched Skills")

        if matched_skills:
            for skill in sorted(matched_skills):
                st.write(f"• {skill}")
        else:
            st.write("No matched skills detected.")

        st.subheader("Missing Skills")

        if missing_skills:
            for skill in sorted(missing_skills):
                st.write(f"• {skill}")
        else:
            st.write("No missing skills.")

        st.subheader("Suggested Improvements")

        if missing_skills and suggestions:
            for item in suggestions:
                st.write(f"• **{item['skill']}** — {item['tip']}")

        elif missing_skills:
            st.write("Suggestions could not be generated for the missing skills.")

        else:
            st.write("Your resume already matches most required skills.")

        
    else:
        st.warning("Please upload/paste a resume and paste the job description.")