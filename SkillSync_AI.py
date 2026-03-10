import streamlit as st
import pandas as pd
from src.preprocess import clean_text
from src.ai.skill_extractor_llm import extract_skills_both
from src.ai.suggestion_llm import generate_suggestions
from src.file_parser import extract_text_from_pdf, extract_text_from_docx


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="SkillSync AI",
    page_icon="🎯",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Gradient Title */

.gradient-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    background: linear-gradient(90deg,#2563EB,#7C3AED);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #64748B;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

/* Skill badges */

.badge-success {
    background-color: #DCFCE7;
    color: #166534;
    padding: 6px 12px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.85rem;
    display: inline-block;
    margin: 4px;
}

.badge-danger {
    background-color: #FEE2E2;
    color: #991B1B;
    padding: 6px 12px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.85rem;
    display: inline-block;
    margin: 4px;
}

/* Score styling */

.score-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1rem 0;
}

.score-text {
    font-size: 3.2rem;
    font-weight: 800;
    color: #2563EB;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown("<div class='gradient-title'>SkillSync AI</div>", unsafe_allow_html=True)

st.markdown(
"<p class='subtitle'>Align your resume with job requirements using AI</p>",
unsafe_allow_html=True
)

st.markdown("---")


# ---------------- INPUT SECTION ----------------

col1, col2 = st.columns(2)


# ---------- Resume Section ----------

with col1:

    st.subheader("📄 Resume")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF or DOCX)",
        type=["pdf", "docx"]
    )

    resume_text = ""

    if uploaded_file is not None:

        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)

        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_text_from_docx(uploaded_file)

        st.success("Resume uploaded successfully")


    with st.expander("Or paste resume text manually"):

        resume_text_manual = st.text_area(
            "Paste resume text here",
            height=200
        )

        if resume_text_manual:
            resume_text = resume_text_manual


# ---------- Job Description ----------

with col2:

    st.subheader("💼 Job Description")

    job_text = st.text_area(
        "Paste the Job Description",
        height=300,
        placeholder="Paste the requirements and responsibilities..."
    )

st.markdown("---")

st.markdown("### 💡 Improve Your Resume")

col1, col2 = st.columns([3,1])

with col1:
    st.info(
        "Want to improve your resume formatting, bullet points, and ATS keywords "
        "before running the analysis?"
    )

with col2:
    if st.button("📄 Resume Guide"):
        st.switch_page("pages/Resume_Tips.py")


# ---------------- ANALYZE BUTTON ----------------

st.markdown("")

btn_col1, btn_col2, btn_col3 = st.columns([1,2,1])

with btn_col2:
    analyze = st.button(
        "🚀 Analyze Resume Match",
        use_container_width=True,
        type="primary"
    )


# ---------------- ANALYSIS ----------------

if analyze:

    if resume_text and job_text:

        with st.spinner("🧠 SkillSync AI is analyzing your resume..."):

            resume_clean = clean_text(resume_text)
            job_clean = clean_text(job_text)

            matched_skills, missing_skills = extract_skills_both(
                resume_clean,
                job_clean
            )

            total_skills = len(matched_skills) + len(missing_skills)

            score = len(matched_skills) / total_skills if total_skills else 0
            score_percent = round(score * 100, 2)

            suggestions = generate_suggestions(missing_skills) if missing_skills else []


        st.markdown("---")

        left, right = st.columns(2)
        
        # ---------- LEFT SIDE ----------

        with left:

            with st.container(border=True):

                st.markdown("### Match Score")

                st.markdown(
                    f"<div class='score-container'><div class='score-text'>{score_percent}%</div></div>",
                    unsafe_allow_html=True
                )

                st.progress(int(score_percent))


            with st.container(border=True):

                st.markdown("### ✅ Matched Skills")

                if matched_skills:

                    badges = "".join(
                        [f"<span class='badge-success'>{skill}</span>"
                         for skill in sorted(matched_skills)]
                    )

                    st.markdown(badges, unsafe_allow_html=True)

                else:
                    st.info("No matched skills detected")


        # ---------- RIGHT SIDE ----------

        with right:

            with st.container(border=True):

                st.markdown("### ❌ Missing Skills")

                if missing_skills:

                    badges = "".join(
                        [f"<span class='badge-danger'>{skill}</span>"
                         for skill in sorted(missing_skills)]
                    )

                    st.markdown(badges, unsafe_allow_html=True)

                else:
                    st.success("Great! No missing skills detected.")


            with st.container(border=True):

                st.markdown("### 📈 Suggested Improvements")

                if suggestions:
                    for item in suggestions:
                        with st.expander(item["skill"].title()):
                            st.write(item["tip"])
                else:
                    st.success("Your resume already matches the job skills well!")

    else:

        st.warning(
            "Please upload or paste a resume and provide a job description."
        )