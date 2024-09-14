def mask_account_card(card_number:[str]) -> [str]:
    """Функция принимает на вход номер карты и возвращает ее маску"""

    return f'{card_number[:-5]}'


def get_date(account_number:[str]) -> [str]:
    """Функция принимает на вход номер счета и возвращает его маску"""

    return f'{account_number[-4:]}'


