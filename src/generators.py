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
        empty_str = str(i)
        while len(empty_str) < 16:
            str_sum = "0" + str(i)
            card_number = f"{str_sum[:4]}{str_sum[4:8]}{str_sum[8:12]}{str_sum[12:16]}"
            yield card_number
