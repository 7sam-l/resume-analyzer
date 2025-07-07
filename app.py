from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Allow frontend to call backend

import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text)
    skills = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return list(set(skills))  # ✅ must return a list


def match_jobs(user_skills):
    with open('jobs.json') as f:
        jobs = json.load(f)
        


    matches = []
    for job in jobs:
        job_skills = set(skill.lower() for skill in job['skills'])
        matched = job_skills.intersection(set(s.lower() for s in user_skills))
        score = len(matched) / len(job_skills) * 100
        if score > 0:
            matches.append({
            "title": job['title'],
            "match_percent": round(score, 2),
            "skills": job['skills']
    })



    return sorted(matches, key=lambda x: x['match_percent'], reverse=True)

    doc = nlp(text)
    skills = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return list(set(skills))

@app.route('/upload', methods=['POST'])
def upload_resume():
    uploaded_file = request.files['resume']
    content = uploaded_file.read().decode('utf-8')
    skills = extract_skills(content)
    job_matches = match_jobs(skills)

    return jsonify({
    "message": "Matched jobs!",
    "matches": job_matches
})



if __name__ == '__main__':
    app.run(debug=True)
