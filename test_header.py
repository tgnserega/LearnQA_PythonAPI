import requests

class TestHeader:
    def test_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        header = dict(response.headers)
        print(header)
        assert response.status_code == 200, "Wrong response status"
        assert 'x-secret-homework-header' in header, "There is no x-secret-homework-header in the response"
        assert header.get('x-secret-homework-header') == 'Some secret value', "The headers value does not match Some secret value"