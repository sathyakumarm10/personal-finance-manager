import json
import os
from datetime import datetime

DATA_FILE = "transactions.json"


def load_transactions():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []


def save_transactions():
    with open(DATA_FILE, "w") as file:
        json.dump(transactions, file, indent=4)


transactions = load_transactions()

categories = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Education",
    "Health",
    "Other"
]


def get_next_id():
    if not transactions:
        return 1

    existing_ids = []

    for transaction in transactions:
        if "id" in transaction:
            existing_ids.append(transaction["id"])

    if not existing_ids:
        return 1

    return max(existing_ids) + 1


def show_menu():
    print("\n================================")
    print("     PERSONAL FINANCE MANAGER")
    print("================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Category Summary")
    print("6. Delete Transaction")
    print("7. Exit")


def add_income():
    try:
        amount = float(input("Enter income amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        description = input("Enter description: ").strip()

        if not description:
            print("Description cannot be empty.")
            return

        transaction = {
            "id": get_next_id(),
            "type": "income",
            "amount": amount,
            "description": description,
            "category": None,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        transactions.append(transaction)
        save_transactions()

        print("Income added successfully!")

    except ValueError:
        print("Invalid amount. Please enter a number.")


def add_expense():
    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        description = input("Enter description: ").strip()

        if not description:
            print("Description cannot be empty.")
            return

        print("\nSelect Category:")

        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        category_input = input(
            "Choose category number or name: "
        ).strip()

        selected_category = None

        # If user enters a number
        if category_input.isdigit():
            category_choice = int(category_input)

            if 1 <= category_choice <= len(categories):
                selected_category = categories[category_choice - 1]

        # If user enters category name
        else:
            for category in categories:
                if category.lower() == category_input.lower():
                    selected_category = category
                    break

        if selected_category is None:
            print("Invalid category.")
            return

        transaction = {
            "id": get_next_id(),
            "type": "expense",
            "amount": amount,
            "description": description,
            "category": selected_category,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        transactions.append(transaction)
        save_transactions()

        print(
            f"Expense added successfully under "
            f"{selected_category}!"
        )

    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def view_transactions():
    if not transactions:
        print("\nNo transactions found.")
        return

    print("\n================ TRANSACTIONS ================")

    for index, transaction in enumerate(transactions, start=1):

        transaction_id = transaction.get("id", index)
        transaction_type = transaction["type"].capitalize()
        amount = transaction["amount"]
        description = transaction["description"]
        date = transaction.get("date", "No date")

        if transaction["type"] == "expense":
            category = transaction.get("category", "Other")

            print(
                f"ID: {transaction_id} | "
                f"{date} | "
                f"{transaction_type} | "
                f"{description} | "
                f"{category} | "
                f"₹{amount:.2f}"
            )

        else:
            print(
                f"ID: {transaction_id} | "
                f"{date} | "
                f"{transaction_type} | "
                f"{description} | "
                f"₹{amount:.2f}"
            )


def show_balance():
    total_income = 0
    total_expenses = 0

    for transaction in transactions:

        if transaction["type"] == "income":
            total_income += transaction["amount"]

        elif transaction["type"] == "expense":
            total_expenses += transaction["amount"]

    balance = total_income - total_expenses

    print("\n========== BALANCE ==========")
    print(f"Total Income:   ₹{total_income:.2f}")
    print(f"Total Expenses: ₹{total_expenses:.2f}")
    print(f"Balance:        ₹{balance:.2f}")


def category_summary():
    category_totals = {}

    for category in categories:
        category_totals[category] = 0

    for transaction in transactions:

        if transaction["type"] == "expense":
            category = transaction.get("category", "Other")
            amount = transaction["amount"]

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += amount

    print("\n========== CATEGORY SUMMARY ==========")

    has_expenses = False

    for category, total in category_totals.items():

        if total > 0:
            print(f"{category}: ₹{total:.2f}")
            has_expenses = True

    if not has_expenses:
        print("No expenses found.")


def delete_transaction():
    if not transactions:
        print("\nNo transactions available.")
        return

    view_transactions()

    try:
        transaction_id = int(
            input("\nEnter transaction ID to delete: ")
        )

        for transaction in transactions:

            if transaction.get("id") == transaction_id:
                transactions.remove(transaction)
                save_transactions()

                print("Transaction deleted successfully!")
                return

        print("Transaction not found.")

    except ValueError:
        print("Please enter a valid transaction ID.")


def main():
    while True:
        show_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_income()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            show_balance()

        elif choice == "5":
            category_summary()

        elif choice == "6":
            delete_transaction()

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-7.")


if __name__ == "__main__":
    main()