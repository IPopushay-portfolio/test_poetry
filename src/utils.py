import json
import logging
import os

from src.external_api import conversion_currency

CURRENT_DIR = os.path.dirname("utils")
LOGS_DIR = os.path.join(CURRENT_DIR, "..", "logs")
log_file_path = os.path.join(LOGS_DIR, "utils.log")
logger = logging.getLogger("utils")
"""Создание объекта логгера"""
file_handler = logging.FileHandler(log_file_path)
"""Создание обработчика"""
logger.setLevel(logging.DEBUG)
"""Установка уровня логгирования"""

file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s : %(message)s")
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

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")


def get_transactions(path_file):
    """Функция для получения данных из json-файла"""
    try:
        logger.info(f"Получение данных из файла {path_file}")
        with open(path_file, "r", encoding="UTF-8") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                logger.error(f"Ошибка при чтении json_файла {path_file}")
                return []
            if len(data) == 0 or type(data) is not list:
                return []
    except FileNotFoundError:
        logger.error(f"Ошибка, файл {path_file} не найден")
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
