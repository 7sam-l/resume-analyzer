# resume-analyzer
# 🧠 Resume Analyzer (AI + Web)

An AI-powered resume analyzer that extracts skills from uploaded `.txt` resumes and matches them to real-world job roles.

---

## 🔍 Features

- 📄 Upload resume files (text only)
- ✨ Extracts keywords using **spaCy NLP**
- ✅ Matches with job descriptions
- 📊 Shows match % and required skills
- 🌐 Built using **Flask**, **HTML/JS**, and **Python**

---

## 📂 How to Run

```bash
# Install required packages
pip install flask flask-cors spacy

# Download the spaCy English model
python -m spacy download en_core_web_sm

# Run the server
python app.py
