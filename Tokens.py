import requests, time
from json.decoder import JSONDecodeError

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

try:
    parsed_response = response.json()
except JSONDecodeError:
    print("Response is not a JSON format")
token_key = parsed_response["token"]
second_key = parsed_response["seconds"]

response_before_task_completed = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token_key})
try:
    parsed_last_response = response_before_task_completed.json()
except JSONDecodeError:
    print("Last response is not a JSON format")
status = parsed_last_response["status"]
print(response_before_task_completed.text)

if status == "Job is NOT ready":
    print(f"Статус верный: {status}, но задача не готова")
else:
    print(f"Статус не верный: {status}")
    quit()

time.sleep(second_key)
print("Задача готова!")

response_after_task_completed = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token_key})
parsed_new_response2 = response_after_task_completed.json()
status = parsed_new_response2["status"]
result = parsed_new_response2["result"]
print(response_after_task_completed.text)

if status == "Job is ready" and result:
    print(f"Статус верный: {status}, result: {result} ")
else:
    print(f"Статус не верный: {status}")
    quit()