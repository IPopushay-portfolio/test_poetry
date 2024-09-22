import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "dict_list, mask_number",
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ],
)
def test_filter_by_state(dict_list, mask_number):
    assert filter_by_state(dict_list) == mask_number


@pytest.mark.parametrize(
    "date_list, mask_number",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2024-09-12T23:23:23.671407", "12.09.2024"),
    ],
)
def test_sort_by_date(date_list, mask_number):
    assert sort_by_date(date_list) == mask_number
