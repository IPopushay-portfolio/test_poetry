import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "transactions, currency_code")

def test_filter_by_currency(transactions, currency_code):
    assert filter_by_currency(transactions, currency_code="USD")


@pytest.mark.parametrize(
    "transactions, description")

def test_transaction_descriptions(transactions, description):
    generator = transaction_descriptions(transactions, description)
    assert next(generator) == "Перевод организации"


@pytest.mark.parametrize(
    "start,finish,expected")

def test_card_number_generator(start, finish, expected):
    assert card_number_generator(start, finish) == expected
