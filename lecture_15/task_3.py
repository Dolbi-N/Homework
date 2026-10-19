import csv

def read_companies():
    with open("ssl_companies.csv", "r") as file:
        reader = csv.DictReader(file)
        companies = []

        for row in reader:
            if int(row["Number of employees"]) > 1000:
                companies.append(row)

        return companies

def save_companies():
    companies = read_companies()

    with open("sorted_companies.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Industry", "Number of employees"])

        for company in companies:
            writer.writerow([
                company["Name"],
                company["Industry"],
                company["Number of employees"]
            ])

save_companies()