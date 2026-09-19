from datetime import datetime

from storage import save_transactions


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


def get_next_id(transactions):
    if not transactions:
        return 1

    existing_ids = []

    for transaction in transactions:
        if "id" in transaction:
            existing_ids.append(transaction["id"])

    if not existing_ids:
        return 1

    return max(existing_ids) + 1


def add_income(transactions):
    try:
        amount = float(
            input("Enter income amount: ₹")
        )

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        description = input(
            "Enter description: "
        ).strip()

        if not description:
            print("Description cannot be empty.")
            return

        transaction = {
            "id": get_next_id(transactions),
            "type": "income",
            "amount": amount,
            "description": description,
            "category": None,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        transactions.append(transaction)

        save_transactions(transactions)

        print("Income added successfully!")

    except ValueError:
        print("Invalid amount. Please enter a number.")


def add_expense(transactions):
    try:
        amount = float(
            input("Enter expense amount: ₹")
        )

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        description = input(
            "Enter description: "
        ).strip()

        if not description:
            print("Description cannot be empty.")
            return

        print("\nSelect Category:")

        for index, category in enumerate(
            categories,
            start=1
        ):
            print(f"{index}. {category}")

        category_input = input(
            "Choose category number or name: "
        ).strip()

        selected_category = None

        if category_input.isdigit():
            category_choice = int(category_input)

            if 1 <= category_choice <= len(categories):
                selected_category = categories[
                    category_choice - 1
                ]

        else:
            for category in categories:
                if (
                    category.lower()
                    == category_input.lower()
                ):
                    selected_category = category
                    break

        if selected_category is None:
            print("Invalid category.")
            return

        transaction = {
            "id": get_next_id(transactions),
            "type": "expense",
            "amount": amount,
            "description": description,
            "category": selected_category,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        transactions.append(transaction)

        save_transactions(transactions)

        print(
            f"Expense added successfully under "
            f"{selected_category}!"
        )

    except ValueError:
        print(
            "Invalid amount. Please enter a valid number."
        )


def view_transactions(transactions):
    if not transactions:
        print("\nNo transactions found.")
        return

    print(
        "\n================ TRANSACTIONS ================"
    )

    for index, transaction in enumerate(
        transactions,
        start=1
    ):
        transaction_id = transaction.get(
            "id",
            index
        )

        transaction_type = transaction[
            "type"
        ].capitalize()

        amount = transaction["amount"]
        description = transaction["description"]

        date = transaction.get(
            "date",
            "No date"
        )

        if transaction["type"] == "expense":
            category = transaction.get(
                "category",
                "Other"
            )

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


def edit_transaction(transactions):
    if not transactions:
        print("\nNo transactions available.")
        return

    view_transactions(transactions)

    try:
        transaction_id = int(
            input(
                "\nEnter transaction ID to edit: "
            )
        )

        selected_transaction = None

        for transaction in transactions:
            if (
                transaction.get("id")
                == transaction_id
            ):
                selected_transaction = transaction
                break

        if selected_transaction is None:
            print("Transaction not found.")
            return

        print(
            "\nLeave a field empty to keep "
            "the current value."
        )

        new_amount = input(
            f"Amount "
            f"[{selected_transaction['amount']}]: ₹"
        ).strip()

        if new_amount:
            amount = float(new_amount)

            if amount <= 0:
                print(
                    "Amount must be greater than 0."
                )
                return

            selected_transaction["amount"] = amount

        new_description = input(
            f"Description "
            f"[{selected_transaction['description']}]: "
        ).strip()

        if new_description:
            selected_transaction[
                "description"
            ] = new_description

        if selected_transaction["type"] == "expense":
            current_category = selected_transaction.get(
                "category",
                "Other"
            )

            print(
                f"\nCurrent category: "
                f"{current_category}"
            )

            print(
                "Press Enter to keep "
                "the current category."
            )

            for index, category in enumerate(
                categories,
                start=1
            ):
                print(
                    f"{index}. {category}"
                )

            category_input = input(
                "New category number or name: "
            ).strip()

            if category_input:
                selected_category = None

                if category_input.isdigit():
                    category_choice = int(
                        category_input
                    )

                    if (
                        1
                        <= category_choice
                        <= len(categories)
                    ):
                        selected_category = categories[
                            category_choice - 1
                        ]

                else:
                    for category in categories:
                        if (
                            category.lower()
                            == category_input.lower()
                        ):
                            selected_category = category
                            break

                if selected_category is None:
                    print("Invalid category.")
                    return

                selected_transaction[
                    "category"
                ] = selected_category

        save_transactions(transactions)

        print(
            "Transaction updated successfully!"
        )

    except ValueError:
        print(
            "Please enter valid numeric values."
        )


def delete_transaction(transactions):
    if not transactions:
        print("\nNo transactions available.")
        return

    view_transactions(transactions)

    try:
        transaction_id = int(
            input(
                "\nEnter transaction ID to delete: "
            )
        )

        for transaction in transactions:
            if (
                transaction.get("id")
                == transaction_id
            ):
                transactions.remove(transaction)

                save_transactions(transactions)

                print(
                    "Transaction deleted successfully!"
                )
                return

        print("Transaction not found.")

    except ValueError:
        print(
            "Please enter a valid transaction ID."
        )