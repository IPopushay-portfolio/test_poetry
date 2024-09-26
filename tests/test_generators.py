import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "transactions, currency_code",
    transactions=(
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
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ),
)
def test_filter_by_currency(transactions, currency_code):
    assert filter_by_currency(transactions, currency_code="USD")


@pytest.mark.parametrize(
    "transactions, description",
    transactions=[
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
    ],
)
def test_transaction_descriptions(transactions, description):
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"


@pytest.mark.parametrize(
    "start,finish,expected",
    {
        1,
        2,
        [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
        ],
    },
)
def test_card_number_generator(start, finish, expected):
    assert card_number_generator(start, finish) == expected
