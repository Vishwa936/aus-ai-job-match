import streamlit as st

st.set_page_config(page_title="Resume Writing Guide", page_icon="💡")

st.title("💡 Resume Writing Guide")

st.markdown("### How to Write a Strong Resume")

tips = [
"Start bullet points with strong action verbs",
"Focus on achievements not responsibilities",
"Use numbers to quantify results",
"Tailor resume to the job description",
"Keep bullet points short",
"Use consistent formatting",
"Highlight most relevant projects first",
"Avoid generic phrases",
"Mention specific technologies used",
"Keep resume ATS friendly"
]

for tip in tips:
    st.markdown(f"• {tip}")