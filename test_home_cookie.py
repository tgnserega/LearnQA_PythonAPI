import requests

class TestHomeCookie:

    def test_home_cookies(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie = dict(response.cookies)
        print(cookie)
        assert response.status_code == 200, "Wrong response status"
        assert 'HomeWork' in cookie, "There is no homework cookie in the response"
        assert cookie.get("HomeWork") == 'hw_value', "The cookie value does not match hw_value"