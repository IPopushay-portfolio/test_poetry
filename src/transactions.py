import csv

import pandas as pd

with open("transactions.csv") as tr_file:
    reader = csv.DictReader(tr_file)
    for row in reader:
        print(row)

df = pd.read_excel(r"C:\\Users\user\\Desktop\\Python\my_prj\\test_poetry\src\\transactions_excel (1).xlsx")
#  ('C:\\Users\user\\Desktop\\Python\my_prj\\test_poetry\src\\transactions_excel (1).xlsx')

# print(df.shape)
# print(df.head())
