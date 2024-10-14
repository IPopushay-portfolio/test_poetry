import json

from src.external_api import conversion_currency


def get_transactions(file):
    try:
        with open(file, encoding="UTF-8") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                return []
            if len(data) == 0 or type(data) != list:
                return []

    return data


def get_sum():
    data = get_transactions("C:\Users\user\Desktop\Python\my_prj\test_poetry\data\operations.json")
    lst_str = []
    amount = []
    for i in data:
        if len(i) == 0:
            continue
        elif i["OperationAmount"]["Currency"]["Code"] != 'RUB':
            conversion_currency('RUB', i["OperationAmount"]["Currency"]["Code"], i["OperationAmount"]["amount"])
            lst_str.append(i["OperationAmount"]["amount"])
            for i in lst_str:
                amount.append(float(i))
            return sum(amount)



if __name__ == '__main__':
    print(conversion_currency('RUB', 'USD', '200000'))




