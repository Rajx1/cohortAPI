from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions
from controllers import students

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Conway API'}), 200

@app.route('/students', methods=['GET', 'POST'])
def students_handler():
    fns = {
        'GET': students.index,
        'POST': students.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/students/<string:student_name>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def student_handler(student_name):
    fns = {
        'GET': students.get_student,
        'PATCH': students.update,
        'PUT': students.update,
        'DELETE': students.destroy
    }
    resp, code = fns[request.method](request, student_name)
    return jsonify(resp), code

if __name__ == "__main__":
    app.run(debug=True)
