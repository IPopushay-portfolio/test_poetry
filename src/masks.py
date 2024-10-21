import logging

logger = logging.getLogger("masks")
"""Создание объекта логгера"""
logger.setLevel(logging.DEBUG)
"""Установка уровня логгирования"""
file_handler = logging.FileHandler("logs/masks.log")
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


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f" **{account_number[-4:]}"
