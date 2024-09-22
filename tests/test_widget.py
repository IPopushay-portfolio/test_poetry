import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "type_num_account, mask_number",
    [
        ("Visa Super Card 1234567890123456", "Visa Super Card 1234 56** **** 3456"),
        ("Maestro 1234578484648788", "Maestro 1234 57** **** 8788"),
        ("Счет 12345678901234567890", "Счет  **7890"),
        ("Счет 13579064547897898745", "Счет  **8745"),
    ],
)
def test_mask_account_card(type_num_account, mask_number):
    assert mask_account_card(type_num_account) == mask_number


@pytest.mark.parametrize(
    "day_pay, mask_number",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2024-09-12T23:23:23.671407", "12.09.2024"),
    ],
)
def test_get_date(day_pay, mask_number):
    assert get_date(day_pay) == mask_number
