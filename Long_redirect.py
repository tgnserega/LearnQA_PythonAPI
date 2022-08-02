import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
all_redirects = response.history
amount_redirects = len(all_redirects)

print("Итоговый url: ", all_redirects[-1].url)
print("Количество редиректов: ", amount_redirects)
