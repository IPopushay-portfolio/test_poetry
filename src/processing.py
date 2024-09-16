def filter_by_state(dict_list, state):
    """Функция принимает список словарей и опционально значение для ключа
    state"""
    list_1 = []
    for i in dict_list:
        if i == state:
            list_1.append(i)
            return list_1


def sort_by_date(list_of_data: list[dict[str]]) -> list:
    """Функция принимает список словарей и необязательный параметр, з
    адающий порядок сортировки (по умолчанию — убывание)."""
    sorted_list = sorted(list_of_data, key=lambda x: x["data"], reverse=True)
    return sorted_list


# print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED',
#                        'date': '2019-07-03T18:35:29.512364'},
#                       {'id': 939719570, 'state': 'EXECUTED',
#                        'date': '2018-06-30T02:08:58.425572'},
#                       {'id': 594226727, 'state': 'CANCELED',
#                        'date': '2018-09-12T21:27:25.241689'},
#                       {'id': 615064591, 'state': 'CANCELED',
#                        'date': '2018-10-14T08:21:33.419441'}], state='EXECUTED'))
