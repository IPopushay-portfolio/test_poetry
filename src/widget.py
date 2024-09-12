import datetime
"""Импортируем библиотеку datetime"""
from src.masks import get_mask_account, get_mask_card_number
"""Импортируем функции из предыдущего ДЗ"""


def mask_account_card(type_num_account:str) -> str:
    """Функция умеет обрабатывать информацию как о картах, так и о счетах"""
    return f'{type_num_account[:4]}{type_num_account[4:6]}** ****{type_num_account[12:]}'




def get_date(day_pay:[str]) -> [str]:
    """Функция принимает на вход строку и отдает корректный результат в формате
11.07.2018"""
    new_day_pay = f'{day_pay.strftime("%d.%m.%Y")}'
    return new_day_pay

