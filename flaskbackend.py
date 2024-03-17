# flask_backend.py

from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    user_question = request.json["user_question"]
    response = subprocess.check_output(["streamlit", "run", "streamlit_app.py", "--", f"--user_question={user_question}"])
    return jsonify({"response": response.decode()})

if __name__ == "__main__":
    app.run(debug=True)
