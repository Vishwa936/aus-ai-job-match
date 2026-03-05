# AI Job Match – Resume to Job Description Matching

AI-powered system that compares a resume with a job description and calculates a match score using NLP techniques such as TF-IDF similarity.

This project is tailored for analysing job matches in the Australian technology job market.

---

## 📌 Problem

Many international graduates in Australia apply to jobs without knowing how well their resume aligns with job descriptions. This often results in low response rates and missed opportunities.

There is a need for a simple, intelligent system that analyzes resume-to-job description alignment and highlights missing skills.

---

## 💡 Solution

A web-based application that:

- Accepts resume text input
- Accepts job description input
- Extracts key skills and keywords
- Calculates similarity score using NLP techniques
- Identifies missing keywords
- Provides actionable improvement suggestions

---
## Example Output

```
Resume: Data Analyst with Python and SQL experience
Job Description: Backend Engineer requiring Python, Docker, AWS

Match Score: 67%

Missing Skills:
- Docker
- AWS

Suggested Improvements:
- Mention backend API development
- Highlight database optimisation experience
```
## Project Structure

```
aus-ai-job-match
│
├ src/              Core implementation of the AI matching system
├ tests/            Unit tests for preprocessing and similarity engine
├ requirements.txt  Python dependencies
└ README.md         Project documentation
```

---
## ⚙️ Tech Stack (Planned)

- **Backend:** Python (initial implementation)
- **NLP:** scikit-learn, TF-IDF similarity
- **Frontend:** Planned (Streamlit / React)
- **Database:** Planned (PostgreSQL)
- **Deployment:** Planned (Render / Railway)
---

## 🚀 MVP Features

- Resume text preprocessing
- Job description keyword extraction
- TF-IDF similarity scoring
- Missing keyword detection
- API endpoint returning match score

---

## Future Improvements

- Replace TF-IDF with embedding models
- Add resume PDF parsing
- Build a simple Streamlit interface
- Integrate with job APIs for real-time analysis
---

## 📂 Project Status

Currently in active development.
