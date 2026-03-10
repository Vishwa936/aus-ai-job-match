# SkillSync AI – Resume ↔ Job Match Analyzer

SkillSync AI is an AI-powered system that analyzes how well a resume matches a job description using NLP and LLM-based skill extraction.

The platform identifies matching skills, missing skills, and provides actionable suggestions to improve resume alignment with job requirements.

---

## Problem

Many graduates apply for jobs without understanding how well their resume aligns with the job description.

This often leads to low interview rates because resumes miss important skills and keywords required by employers.

---

## Solution

SkillSync AI analyzes resumes against job descriptions and provides intelligent feedback.

The system:

• Extracts skills from resumes and job descriptions  
• Calculates resume-to-job alignment score  
• Identifies missing skills  
• Generates improvement suggestions  
• Provides resume writing tips  

---

## Features

• Resume upload (PDF or DOCX)  
• Manual resume text input  
• Job description analysis  
• AI skill extraction  
• Match score calculation  
• Missing skill detection  
• AI improvement suggestions  
• Resume writing guide  

---

## Example Output
Match Score: 67%

Matched Skills
Python, SQL, Data Analysis

Missing Skills
Docker, AWS

Suggested Improvements
Add cloud deployment experience and containerization projects.

---

## Tech Stack

Backend  
• Python  

AI / NLP  
• Sentence Transformers  
• LLM-based skill extraction  

Frontend  
• Streamlit  

Utilities  
• PDF parsing  
• DOCX parsing  

---

## Project Structure

'''
SkillSync-AI
│
├── SkillSync_AI.py Main Streamlit application
├── requirements.txt
│
├── pages
│ └── Resume_Tips.py
│
├── src
│ ├── preprocess.py
│ ├── file_parser.py
│ ├── similarity.py
│ ├── ai
│ │ ├── skill_extractor_llm.py
│ │ └── suggestion_llm.py
│
└── tests
'''

---

## Future Improvements

• Resume rewriting suggestions using LLM  
• Job application tracking dashboard  
• User accounts and resume storage  
• Analytics dashboard for skill gaps  
• Integration with job APIs  

---

## Deployment

The application can be deployed using:

• Streamlit Community Cloud  
• Render  
• Railway  

---

## Project Status

Active development.

Version 1 includes AI-powered resume-to-job matching with skill analysis and improvement suggestions.
