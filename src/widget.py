import datetime
import masks

"""Импортируем библиотеку datetime"""


def mask_account_card(type_num_account: [str]) -> [str]:
    """Функция умеет обрабатывать информацию как о картах, так и о счетах"""
    card_number = "".join(el if el.isdigit() else "" for el in type_num_account)
    number_card_mask = mask_account_card(card_number)
    name_card = "".join("" if el.isdigit() else el for el in type_num_account)
    data_card_mask = name_card + number_card_mask
    return data_card_mask


def get_date(day_pay: [str]) -> [str]:
    """Функция принимает на вход строку и отдает корректный результат в формате
    11.07.2018"""
    date_format = day_pay.strptime(day_pay, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
