import json
import logging
import os

PATH_FILE = os.path.abspath("../data/operations.json")

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


def login(path_file: str) -> list:
    """Записываем информацию о попытке открытия файла"""
    try:
        logger.info(f"Попытка входа для пользователя: {path_file}")
        """Проверяем правильность входа пользователя"""
        with open(path_file, "r", encoding="UTF-8") as file:
            operations = json.load(file)
            return operations
    except FileNotFoundError:
        logger.error(f'Ошибка при чтении: "{path_file}"')
        return []
