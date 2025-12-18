import csv
import os

FILE_NAME = "students.csv"


def export_data(students):
    if not students:
        print("No data to export.")
        return

    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["name", "section", "spanish", "english", "socials", "science", "average"]
        )

        for s in students:
            writer.writerow([
                s["name"],
                s["section"],
                s["spanish"],
                s["english"],
                s["socials"],
                s["science"],
                s["average"]
            ])

    print("Data exported to students.csv")


def import_data():
    if not os.path.exists(FILE_NAME):
        print("No CSV file found. Export data first.")
        return []

    data = []
    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["spanish"] = float(row["spanish"])
            row["english"] = float(row["english"])
            row["socials"] = float(row["socials"])
            row["science"] = float(row["science"])
            row["average"] = float(row["average"])
            data.append(row)

    print("Data imported successfully!")
    return data
