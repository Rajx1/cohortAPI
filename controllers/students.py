''' Students controller '''
from werkzeug.exceptions import BadRequest

students = [
    {"id": 1, "name": "Emily"},
    {"id": 2, "name": "Angela"},
    {"id": 3, "name": "Guy"},
    {"id": 4, "name": "Raj"},
]


def index(req):
    return [student for student in students], 200

def create(req):
    new_student = req.get_json()
    new_student["id"] = sorted([student["id"] for student in students])[-1] + 1
    students.append(new_student)
    return new_student, 201

def update(req, name):
    keys = ["name", "favourite_food", "age", "last_holiday", "ninja_or_pirate"]
    student = find_by_name(name)
    data = req.get_json()
    for key, val in data.items():
        if key not in keys:
            keys_string = ", ".join(keys)
            raise BadRequest(f"You can only add the following data: {keys_string}")
    for key, val in data.items():
        student[key] = val
    return student, 200

def destroy(req, name):
    student = find_by_name(name)
    students.remove(student)
    return {"msg": f"{name} was deleted"}, 200

def get_student(req, name):
    student = find_by_name(name)
    return student, 200

def find_by_name(name):
    try:
        return next(student for student in students if student['name'].lower() == name.lower())
    except:
        raise BadRequest(f"We don't have a student called {name}!")