import csv
vips = []
newbies = []
regualrs = []
with open("C:\\Users\\acer\\Desktop\\Coding\\Python\\data projects\\ages\\customers.csv", newline="", encoding="utf-8") as user:

    man = csv.DictReader(user)

    for row in man:
        if row["Age"] and row["City"]:
          print(row)
