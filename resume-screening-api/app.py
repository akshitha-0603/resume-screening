from flask import Flask, request, jsonify
from model import predict_role

app = Flask(__name__)

# Home route (to check API is running)
@app.route("/")
def home():
    return "Resume Screening API is Running"

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()   # get input from user
    skills = data["skills"]     # extract skills

    role, score = predict_role(skills)  # call model

    return jsonify({
        "input_skills": skills,
        "recommended_role": role,
        "match_score": f"{score}%"
    })

# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)