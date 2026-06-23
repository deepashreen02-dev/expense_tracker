from tracker import (
    create_csv_if_not_exists,
    add_expense,
    view_expenses,
    total_expenses
)


def main():
    create_csv_if_not_exists()

    while True:
        print("\n===== EXPENSE TRACKER MENU =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description: ")

                add_expense(amount, category, description)
                print("✅ Expense added successfully!")

            except ValueError:
                print("❌ Invalid amount!")

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total = total_expenses()
            print(f"\n💰 Total Expenses = Rs.{total:.2f}")

        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice! Try again.")


if __name__ == "__main__":
    main()