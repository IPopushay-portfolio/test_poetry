list_of_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(dict_list: list, state_id="EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа
    state"""
    new_list = []
    for key in dict_list:
        if key.get("state") == state_id:
            new_list.append(key)
    return new_list


def sort_by_date(date_list: list) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)."""
    sorted_list = sorted(date_list, key=lambda x: x["date"], reverse=True)
    return sorted_list


# print(filter_by_state(list_of_dict))
# print(sort_by_date(list_of_dict))
