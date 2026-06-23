import csv
import os
from datetime import datetime

CSV_FILE = "expenses.csv"


def create_csv_if_not_exists():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])


def add_expense(amount, category, description, date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, f"{amount:.2f}", category, description])


def view_expenses():
    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) <= 1:
                print("No expenses recorded yet!")
                return

            print("\n===== YOUR EXPENSES =====")
            print(f"{'No':<4}{'Date':<12}{'Amount':<10}{'Category':<15}Description")

            for i, row in enumerate(rows[1:], start=1):
                date, amount, category, description = row
                print(f"{i:<4}{date:<12}{amount:<10}{category:<15}{description}")

    except FileNotFoundError:
        print("No expenses recorded yet!")


def total_expenses():
    total = 0.0

    try:
        with open(CSV_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                try:
                    total += float(row[1])
                except:
                    continue

        return total

    except FileNotFoundError:
        return 0.0