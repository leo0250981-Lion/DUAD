import csv
import os

FILE_NAME = "students.csv"

def export_data(students):
    if not students:
        print("No data to export.")
        return

    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "section", "spanish", "english", "socials", "science", "average"])
        for s in students:
            writer.writerow(s.values())
    print("Data exported to students.csv")


def import_data():
    if not os.path.exists(FILE_NAME):
        print("No CSV file found. Export data first.")
        return None

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            row["spanish"] = float(row["spanish"])
            row["english"] = float(row["english"])
            row["socials"] = float(row["socials"])
            row["science"] = float(row["science"])
            row["average"] = float(row["average"])
            data.append(row)
        print("Data imported successfully!")
        return data