import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, mask_number",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234578484648788", "1234 57** **** 8788"),
    ],
)
def test_get_mask_card_number(card_number, mask_number):
    assert get_mask_card_number(card_number) == mask_number


@pytest.mark.parametrize(
    "account_number, mask_number",
    [
        ("12345678901234567890", " **7890"),
        ("13579064547897898745", " **8745"),
    ],
)
def test_get_mask_account(account_number, mask_number):
    assert get_mask_account(account_number) == mask_number
