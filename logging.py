import datetime
import os

import requests


class Logger():
    file_name = f"../logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_log_to_file(cls, data: str):
        """Метод который записывает логи"""
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')  # названия теста который выполняется сейчас.

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"  # имя теста
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"  # время теста
        data_to_add += f"Request method: {method}\n"  # названия метода в котором вызываем
        data_to_add += f"Request URL: {url}\n"  # текущая юрла
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)  #  записывваем данные в файл

    @classmethod
    def add_response(cls, response):
        cookies_as_dict = dict(response.cookies)  # достаем куки
        headers_as_dict = dict(response.headers)  #  достаем заголовки

        data_to_add = f"Response code: {response.status_code}\n"
        data_to_add += f"Response text: {response.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"  # записываем заголовки
        data_to_add += f"Response cookies: {cookies_as_dict}\n"  # записываем куки
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)



Logger.add_request(method="GET", url="https://google.com")
response = requests.request(method="GET", url="https://google.com")
print(response.headers)
print(response.cookies)
print(response.text)
print(response.status_code)
Logger.add_response(response)
