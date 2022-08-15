from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure


@allure.epic("Edition cases")
@allure.feature("Edition")
class TestEdit(BaseCase):
    @allure.title("Test edit just created user (successful)")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test edit user after creation")
    def test_edit_just_created_user(self):
        # REG
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        first_name = register_data["firstName"]
        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # EDIT
        new_name = "Changed name"
        response3 = MyRequests.put(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid}, data={'firstName': new_name})
        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of the user after edit")

    @allure.title("Edit user without authorization")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test doesn't edit user without authorization")
    def test_edit_user_not_auth(self):
        # REG
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        first_name = register_data["firstName"]
        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # EDIT
        new_name = "Changed name"
        response3 = MyRequests.put(f"/user/{user_id}", data={'firstName': new_name})
        Assertions.assert_code_status(response3, 400)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})
        Assertions.assert_json_value_by_name(response4, "firstName", first_name, "Wrong name of the user after edit without authorization")

    @allure.title("Edit user with authorization as another user")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Test doesn't edit user with authorization as another user")
    def test_edit_with_another_user(self):
        # REG USER1
        register_data_1 = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data_1)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        first_name_1 = register_data_1["firstName"]
        email_1 = register_data_1["email"]
        password_1 = register_data_1["password"]
        user_id_1 = self.get_json_value(response1, "id")

        # REG USER2
        register_data_2 = self.prepare_registration_data()
        response2 = MyRequests.post("/user/", data=register_data_2)
        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        first_name_2 = register_data_2["firstName"]
        email_2 = register_data_2["email"]
        password_2 = register_data_2["password"]
        user_id_2 = self.get_json_value(response2, "id")

        # LOGIN USER1
        login_data_1 = {
            'email': email_1,
            'password': password_1
        }
        response3 = MyRequests.post("/user/login", data=login_data_1)
        auth_sid_1 = self.get_cookie(response3, 'auth_sid')
        token_1 = self.get_header(response3, 'x-csrf-token')

        # LOGIN USER2
        login_data_2 = {
            'email': email_2,
            'password': password_2
        }
        response4 = MyRequests.post("/user/login", data=login_data_2)
        auth_sid_2 = self.get_cookie(response4, 'auth_sid')
        token_2 = self.get_header(response4, 'x-csrf-token')

        # EDIT
        new_name = "Changed name"
        response5 = MyRequests.put(f"/user/{user_id_1}", headers={'x-csrf-token': token_2}, cookies={'auth_sid': auth_sid_2}, data={'firstName': new_name})
        Assertions.assert_code_status(response5, 200)

        # GET USER1
        response6 = MyRequests.get(f"/user/{user_id_1}", headers={'x-csrf-token': token_1}, cookies={'auth_sid': auth_sid_1})
        Assertions.assert_json_value_by_name(response6, "firstName", first_name_1, "Wrong name of the user 1 after edit with different user")

    @allure.title("Edit user email to email without '@'")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test doesn't edit user email to email without '@'")
    def test_edit_user_email_to_bad_email(self):
        # REG
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        first_name = register_data["firstName"]
        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # EDIT
        new_email = "learnqaexample.com"
        response3 = MyRequests.put(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid}, data={'email': new_email})
        Assertions.assert_code_status(response3, 400)
        assert response3.text == 'Invalid email format', "Unexpected response text for invalid email"

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})
        Assertions.assert_json_value_by_name(response4, "email", email, "Wrong email of the user after edit")

    @allure.title("Edit user name to too short name")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test doesn't edit user name to too short name")
    def test_edit_user_name_to_short_name(self):
        # REG
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        first_name = register_data["firstName"]
        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        # EDIT
        new_name = "X"
        response3 = MyRequests.put(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid}, data={'firstName': new_name})
        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_value_by_name(response3, "error", "Too short value for field firstName", "Unexpected response for too short name")

        # GET
        response4 = MyRequests.get(f"/user/{user_id}", headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})
        Assertions.assert_json_value_by_name(response4, "firstName", first_name, "Wrong email of the user after edit")