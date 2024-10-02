def filter_by_currency(usd_transactions, currency_code="USD"):
    """Функция выдает транзакции, где валюта операции соответствует заданной."""

    try:
        for i in usd_transactions:
            if i.get("operationAmount").get("currency").get("code") == currency_code:
                yield i
    except StopIteration:
        if usd_transactions == "":
            return "Нет транзакций"


def transaction_descriptions(description):
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    try:
        for description_operation in description:
            yield description_operation.get("description")
    except StopIteration:
        if description == "":
            return "Нет транзакций"


def card_number_generator(start, finish):
    """Создан генератор, который выдает номера банковских карт"""
    for i in range(start, finish + 1):
        number = f"{i:016}"
        card_number = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:16]}"
        yield card_number


# for card_number in card_number_generator(1, 20):
#    print(card_number)
