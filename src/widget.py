import datetime
from typing import Union
import masks
"""Импортируем библиотеку datetime"""

def mask_account_card(type_num_account: [str]) -> [str]:
    """Функция умеет обрабатывать информацию как о картах, так и о счетах"""
    if "Счет" in type_num_account:
        account = type_num_account[-22:]
        return type_num_account[:4] + masks.get_mask_account(account)
    else:
        number_card = "".join(type_num_account[-16:].split())
        return type_num_account[:-16] + masks.get_mask_card_number(number_card)


def get_date(day_pay: [str]) -> [str]:
    """Функция принимает на вход строку с датой в формате  и возвращает строку с датой"""
    return f"{day_pay[8:10]}.{day_pay[5:7]}.{day_pay[:4]}"


# print(mask_account_card('Visa Super Card 1234567890123456')) # выведет "Visa Super Card 1234 56** **** 3456"
# print(mask_account_card('Maestro 1234578484648788')) # выведет "Maestro 1234 57** **** 8788"

# print(mask_account_card('Счет 12345678901234567890')) # выведет "Счет **7890"
# print(mask_account_card('Счет 13579064547897898745')) # выведет "Счет **8745"

# print(get_date('2018-07-11T02:26:18.671407')) # выведет "11.07.2018"
# print(get_date('2024-09-12T23:23:23.671407')) # выведет "12.09.2024"
