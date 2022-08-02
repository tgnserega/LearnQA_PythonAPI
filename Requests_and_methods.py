import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()


print(Fore.GREEN + "\n1. Делаем http-запрос любого типа без параметра method:")

response_without_parameter = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(Fore.LIGHTWHITE_EX + "Запрос без параметра: ", response_without_parameter.text, "\nСтатус код: ", response_without_parameter.status_code)

print(Fore.GREEN +"\n2. Делаем http-запрос не из списка - HEAD:")
response_not_from_the_list = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(Fore.LIGHTWHITE_EX + "Запрос не из списка: ", response_not_from_the_list.text, "\nСтатус код: ", response_not_from_the_list.status_code)

print(Fore.GREEN +"\n3. Делаем запрос с правильным значением method:")
correct_response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(Fore.LIGHTWHITE_EX + "Корректный запрос: ", correct_response.text, "\nСтатус код: ", correct_response.status_code)

print(Fore.GREEN +"\n4. С помощью цикла проверяем все возможные сочетания реальных типов запроса и значений параметра method:")
print(Style.RESET_ALL)
methods = ["GET", "POST", "PUT", "DELETE"]

for method in methods:
    for i in methods:
        if i == "GET":
            print("\n")
            response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={'method': method})
            print(f"Тип запроса {i}, метод {method}, статус код {response.status_code}")
            print(f"Ответ: {response.text}")
            if i != method and response.text == '{"success":"!"}':
                print(Fore.RED +f"Параметр {i} и тип {method} не совпадают, но возвращают успешный результат")
                print(Style.RESET_ALL)
            if i == method and response.text != correct_response.text:
                print(Fore.RED +f"Параметр {i} и тип {method} совпадают, но возвращают не успешный результат")
                print(Style.RESET_ALL)
        elif i == "POST":
            response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': method})
            print(f"Тип запроса {i}, метод {method}, статус код {response.status_code}")
            print(f"Ответ:  {response.text}")
            if i != method and response.text == correct_response.text:
                print(Fore.RED +f"Параметр {i} и тип {method} не совпадают, но возвращают успешный результат")
                print(Style.RESET_ALL)
            if i == method and response.text != correct_response.text:
                print(Fore.RED +f"Параметр {i} и тип {method} совпадают, но возвращают не успешный результат")
                print(Style.RESET_ALL)

        elif i == "PUT":
            response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': method})
            print(f"Тип запроса {i}, метод {method}, статус код {response.status_code}")
            print(f"Ответ:  {response.text}")
            if i != method and response.text == correct_response.text:
                print(Fore.RED +f"Параметр {i} и тип {method} не совпадают, но возвращают успешный результат")
                print(Style.RESET_ALL)
            if i == method and response.text != correct_response.text:
                print(Fore.RED +f"Параметр {i} и тип {method} совпадают, но возвращают не успешный результат")
                print(Style.RESET_ALL)
        elif i == "DELETE":
            response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={'method': method})
            print(f"Тип запроса {i}, метод {method}, статус код {response.status_code}")
            print(f"Ответ:  {response.text}")
            if i != method and response.text == correct_response.text:
                print(Fore.RED +f"Параметр {i} и тип {method} не совпадают, но возвращают успешный результат")
                print(Style.RESET_ALL)
            if i == method and response.text != correct_response.text:
                print(Fore.RED +f"Параметр {i} и тип {method} совпадают, но возвращают не успешный результат")
                print(Style.RESET_ALL)


