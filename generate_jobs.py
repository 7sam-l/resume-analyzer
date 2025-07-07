import json

jobs = [
    ("Data Scientist", ["Python", "Machine Learning", "Pandas"]),
    ("Frontend Developer", ["HTML", "CSS", "JavaScript", "React"]),
    ("Backend Developer", ["Node.js", "Express", "MongoDB"]),
    ("AI Engineer", ["Python", "TensorFlow", "Deep Learning"]),
    ("Mobile App Developer", ["Flutter", "Dart", "Firebase"]),
    ("Cloud Engineer", ["AWS", "Docker", "Kubernetes"]),
    ("DevOps Engineer", ["CI/CD", "Linux", "Git"]),
    ("Cybersecurity Analyst", ["Network Security", "Firewalls", "Threat Detection"]),
    ("UI/UX Designer", ["Figma", "Wireframes", "Design Systems"]),
    ("Full Stack Developer", ["React", "Node.js", "SQL", "REST"]),
    ("Data Analyst", ["SQL", "Excel", "Tableau", "Pandas"]),
    ("Game Developer", ["Unity", "C#", "Game Physics"]),
    ("ML Researcher", ["NLP", "PyTorch", "Transformers"]),
    ("Technical Writer", ["Documentation", "Markdown", "GitHub"]),
    ("Blockchain Developer", ["Solidity", "Ethereum", "Smart Contracts"])
]

# Write to jobs.json
with open("jobs.json", "w") as f:
    json.dump([{"title": title, "skills": skills} for title, skills in jobs], f, indent=2)

print("✅ jobs.json created with 15 job entries.")
