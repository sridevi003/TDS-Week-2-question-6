import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the student data
with open("api/student_marks.json") as f:
    student_marks = json.load(f)

@app.route("/api")
def get_marks():
    # Get names from the query parameters
    names = request.args.getlist('name')
    marks = []

    # Find marks for each name
    for name in names:
        if name in student_marks:
            marks.append(student_marks[name])
        else:
            marks.append(None)  # or return a default value if name is not found

    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
