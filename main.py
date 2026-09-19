from storage import load_transactions

from transactions import (
    add_income,
    add_expense,
    view_transactions,
    edit_transaction,
    delete_transaction
)

from reports import (
    show_balance,
    category_summary
)


transactions = load_transactions()


def show_menu():
    print("\n================================")
    print("     PERSONAL FINANCE MANAGER")
    print("================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Category Summary")
    print("6. Edit Transaction")
    print("7. Delete Transaction")
    print("8. Exit")


def main():
    while True:
        show_menu()

        choice = input(
            "\nChoose an option: "
        ).strip()

        if choice == "1":
            add_income(transactions)

        elif choice == "2":
            add_expense(transactions)

        elif choice == "3":
            view_transactions(transactions)

        elif choice == "4":
            show_balance(transactions)

        elif choice == "5":
            category_summary(transactions)

        elif choice == "6":
            edit_transaction(transactions)

        elif choice == "7":
            delete_transaction(transactions)

        elif choice == "8":
            print("\nGoodbye!")
            break

        else:
            print(
                "Invalid choice. Please choose 1-8."
            )


if __name__ == "__main__":
    main()