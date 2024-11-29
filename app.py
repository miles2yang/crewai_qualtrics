from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "CrewAI-Qualtrics integration is running!"

@app.route("/distribute", methods=["POST"])
def distribute_survey():
    data = request.json
    survey_id = data.get("survey_id")
    contact_list_id = data.get("contact_list_id")
    if not survey_id or not contact_list_id:
        return jsonify({"error": "Missing survey_id or contact_list_id"}), 400
    return jsonify({"status": "success", "message": f"Survey {survey_id} sent to list {contact_list_id}"})
