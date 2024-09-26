import pytest

@pytest.fixture
def test_filter_by_currency(transactions, currency_code):
    return transactions, currency_code

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
    )
@pytest.fixture
def test_transaction_descriptions(transactions, description):
    return transactions, description
transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},]


@pytest.fixture
def test_card_number_generator(expected):
    return expected
expected = (["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004",
        "0000 0000 0000 0005",], )