import json
import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_skills_both(resume_text, job_text):

    prompt = f"""
You are an expert AI resume analyzer.

Compare the resume with the job description and determine whether the resume
demonstrates the key skills required for the job.

Focus on the **important technical or professional skills mentioned in the job description**.

For each important skill, determine if the resume shows evidence of that skill,
even if the wording is different.

Examples:
- Tableau or Power BI → data visualization
- AWS EC2 / S3 / Lambda → AWS
- Flask or Django APIs → REST APIs
- Pandas / NumPy usage → data analysis

Rules:
- Focus on job-relevant skills
- Avoid duplicates
- Use concise skill names
- Ignore soft skills unless explicitly required
- If related technology implies the skill, consider it matched

Return JSON only.

FORMAT:

{{
 "matched_skills": [],
 "missing_skills": []
}}

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You analyze resumes and job descriptions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    json_match = re.search(r"\{.*\}", content, re.DOTALL)

    if not json_match:
        return set(), set()

    data = json.loads(json_match.group())

    matched = set(s.lower() for s in data["matched_skills"])
    missing = set(s.lower() for s in data["missing_skills"])

    return matched, missing