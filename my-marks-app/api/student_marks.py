import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load student marks from the JSON file
with open('student_marks.json', 'r') as file:
    student_marks = json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [student_marks.get(name, 'Not found') for name in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
