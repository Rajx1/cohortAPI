import json

class TestApi():
    def test_home(self, api):
        res = api.get("/")
        assert res.status == "200 OK"
        assert res.json["message"] == 'Welcome to the Conway API'
    
    def test_get_students(self, api):
        res = api.get("/students")
        assert res.status == "200 OK"
        assert len(res.json) == 2

    def test_add_student(self, api):
        mock_data = json.dumps({"name": "Test Student 3"})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.post("/students", data=mock_data, headers=mock_headers)
        assert res.status == "201 CREATED"
        assert res.json["id"] == 3

    def test_get_student(self, api):
        res = api.get("/students/test student 1")
        assert res.status == '200 OK'
        assert res.json["name"].lower() == 'test student 1'

    def test_get_student_fail(self, api):
        res = api.get("/students/test student 5")
        assert res.status == '400 BAD REQUEST'
        assert "We don't have a student called test student 5!" in res.json["message"]
    
    def test_update_student(self, api):
        mock_data = json.dumps({"age": 28})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.put("/students/test student 1", data=mock_data, headers=mock_headers)
        assert res.status == '200 OK'
        assert res.json["age"] == 28

    def test_update_student_fail(self, api):
        mock_data = json.dumps({"hobby": "chess"})
        mock_headers = {'Content-Type': 'application/json'}
        res = api.put("/students/test student 1", data=mock_data, headers=mock_headers)
        assert res.status == '400 BAD REQUEST'
        assert "You can only add the following data" in res.json["message"]

    def test_delete_student(self, api):
        res = api.delete("/students/test student 1")
        assert res.status == "200 OK"
        assert res.json["msg"] == "test student 1 was deleted"
        
    def test_not_found(self, api):
        res = api.get('/cats')
        assert res.status == '404 NOT FOUND'
        assert 'Oops!' in res.json['message']

