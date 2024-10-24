import logging
import os

CURRENT_DIR = os.path.dirname("masks")
LOGS_DIR = os.path.join(CURRENT_DIR, "..", "logs")
log_file_path = os.path.join(LOGS_DIR, "masks.log")
logger = logging.getLogger("masks")
"""Создание объекта логгера"""
logger.setLevel(logging.DEBUG)
"""Установка уровня логгирования"""
file_handler = logging.FileHandler(log_file_path)
"""Создание обработчика"""
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


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info("Маскируем карту клиента")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


print(get_mask_card_number(str(7000792289606361)))


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.info("Маскируем счет клиента")
    return f" **{account_number[-4:]}"
