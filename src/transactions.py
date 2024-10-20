import csv

with open("transactions.csv") as tr_file:
    reader = csv.DictReader(tr_file)
    for row in reader:
        print(row)


import pandas as pd

df = pd.read_excel("C:\\Users\\user\\Desktop\\Python\\my_prj\\test_poetry\\src.xlsx")

print(df.shape)
print(df.head())
