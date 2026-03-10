import json
import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_suggestions(missing_skills):

    if not missing_skills:
        return []

    skills_list = ", ".join(sorted(missing_skills))

    prompt = f"""
You are a career advisor helping improve resumes.

For each missing skill below, provide ONE short suggestion
for how someone could demonstrate that skill in a project.

Return results in this format:

skill | suggestion

Example:

docker | Containerize a Python application using Docker.
aws | Deploy a REST API project on AWS.

Missing skills:
{skills_list}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You generate resume improvement suggestions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content.strip()

    suggestions = []

    for line in content.split("\n"):
        if "|" in line:
            skill, tip = line.split("|", 1)
            suggestions.append({
                "skill": skill.strip(),
                "tip": tip.strip()
            })

    return suggestions