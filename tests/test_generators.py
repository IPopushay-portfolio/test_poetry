import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


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
        },
    ]


@pytest.mark.parametrize("currency_code", ["USD"])
def test_filter_by_currency(usd_transactions, currency_code):
    generator = filter_by_currency(currency_code, ["USD"])
    assert next(generator) == currency_code


@pytest.fixture
def descriptions():
    return [
        {"description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
    ]


@pytest.mark.parametrize("description", ["Перевод организации"])
def test_transaction_descriptions(description):
    generator = transaction_descriptions(description)
    assert next(generator) == description


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
    generator = card_number_generator(card_number, ["0000 0000 0000 0001"])
    assert next(generator) == card_number
