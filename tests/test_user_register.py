import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic("Registration cases")
@allure.feature("Registration")
class TestUserRegister(BaseCase):
    exclude_params = [
        "username",
        "firstName",
        "lastName",
        'email',
        "password"
    ]

    @allure.title("Register user")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test register user")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.title("Register user with existing email")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test doesn't register user with existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

    @allure.title("Register user with email without '@'")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test doesn't register user with email without '@'")
    def test_create_user_with_incorrect_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", \
            f"Unexpected response content {response.content}"

    @allure.title("Register user without one of parameter")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test doesn't register user without one of parameter")
    @pytest.mark.parametrize('param', exclude_params)
    def test_create_user_without_one_of_parameter(self, param):
        data = self.prepare_registration_data()
        del data[param]
        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {param}", \
            f"Unexpected response content {response.content} with exclude param: {param}"

    @allure.title("Register user with too short name")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test doesn't register user with too short name")
    def test_create_user_with_short_name(self):
        data = self.prepare_registration_data()
        data['firstName'] = 'Y'
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too short", \
            f"Unexpected response content for field 'firstName' when it is too short"

    @allure.title("Register user with too long name")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test doesn't register user with too long name")
    def test_create_user_with_long_name(self):
        data = self.prepare_registration_data()
        long_name = ""
        while len(long_name) <= 250:
            long_name += "Y"
        data['firstName'] = long_name
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'firstName' field is too long", \
            f"Unexpected response content for field 'firstName' when it is too long"
