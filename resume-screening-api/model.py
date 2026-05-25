def predict_role(skills):

    skills = skills.lower()
    score = 0

    if "python" in skills:
        score += 30

    if "machine learning" in skills:
        score += 40

    if "sql" in skills:
        score += 20

    if "excel" in skills:
        score += 10

    if score >= 70:
        role = "Data Scientist"
    elif score >= 40:
        role = "Data Analyst"
    else:
        role = "Intern"

    return role, score