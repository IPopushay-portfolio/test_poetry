import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def usd_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
        },
    ]


@pytest.mark.parametrize("currency_code", ("USD", "RUB"))
def test_filter_by_currency(currency_code, usd_transactions):
    generator = filter_by_currency(usd_transactions, currency_code)
    for usd_transactions in generator:
        assert usd_transactions["operationAmount"]["currency"]["code"] == currency_code


# @pytest.mark.parametrize("description")
def test_transaction_descriptions(usd_transactions):
    expected = ["Перевод организации", "Открытие вклада"]
    generator = transaction_descriptions(usd_transactions)
    assert list(generator) == expected


@pytest.fixture
def card_number():
    return [
        {
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
        },
    ]


@pytest.mark.parametrize("card_number", ["0000 0000 0000 0001"])
def test_card_number_generator(card_number):
    expected = card_number
    generator = card_number_generator(1, 4)
    assert next(generator) == expected
