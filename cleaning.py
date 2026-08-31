import csv
with open("customers.csv", newline="", encoding="utf-8") as user:

    man = csv.DictReader(user)

    for row in man:
        if row["Age"] and row["City"]:
          print(row)
