import requests

payload = {"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/get_text", params=payload)
print(response.text)