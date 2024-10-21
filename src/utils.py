import json
import logging

from src.external_api import conversion_currency

logger = logging.getLogger("utils")
"""Создание объекта логгера"""
logger.setLevel(logging.DEBUG)
"""Установка уровня логгирования"""
file_handler = logging.FileHandler("logs/utils.log")
"""Создание обработчика"""
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(Levelname)s : %(message)s")
"""Создание форматтера"""
file_handler.setFormatter(file_formater)
"""Привязка форматтера к обработчику"""
logger.addHandler(file_handler)
"""Привязка обработчика к логгеру"""
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="application.log",
    filemode="w",
)


def get_transactions(file):
    try:
        with open(file, encoding="UTF-8") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                return []
            if len(data) == 0 or type(data) is not list:
                return []
    except FileNotFoundError:
        return []


def get_sum():
    data = get_transactions("C:\\Users\\user\\Desktop\\Python\\my_prj\\test_poetry\\data\\operations.json")
    lst_str = []
    amount = []
    for i in data:
        if len(i) == 0:
            continue
        elif i["OperationAmount"]["Currency"]["Code"] != "RUB":
            conversion_currency("RUB", i["OperationAmount"]["Currency"]["Code"], i["OperationAmount"]["amount"])
            lst_str.append(i["OperationAmount"]["amount"])
            for j in lst_str:
                amount.append(float(j))
            return sum(amount)


if __name__ == "__utils__":
    print(conversion_currency("RUB", "USD", "200000"))
