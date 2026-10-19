import csv

def read_titanic():
    with open("titanic.csv", "r") as file:
        reader = csv.DictReader(file)
        survivors = []

        for row in reader:
            if row["Survived"] == "1":
                survivors.append(row)

        return survivors


def save_survivors():
    survivors = read_titanic()

    if survivors:
        with open("survived.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=survivors[0].keys())
            writer.writeheader()
            writer.writerows(survivors)

save_survivors()