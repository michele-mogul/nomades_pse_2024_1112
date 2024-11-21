import csv
import os

CSV_FIELDNAMES = ["uid", "pwd", "salt"]


def ensure_csv_file_exists(CSV_PATH):
    """Ensures the CSV file exists with a header row."""
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDNAMES)
            writer.writeheader()


def read_users(CSV_PATH):
    """Reads users from the CSV file and returns a list of dictionaries."""
    ensure_csv_file_exists(CSV_PATH)
    with open(CSV_PATH, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)


def write_user(CSV_PATH, uid, pwd, salt):
    """Writes a new user to the CSV file."""
    ensure_csv_file_exists(CSV_PATH)
    with open(CSV_PATH, "a", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDNAMES)
        writer.writerow({"uid": uid, "pwd": pwd, "salt": salt})
