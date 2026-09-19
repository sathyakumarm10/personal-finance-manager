from transactions import categories


def show_balance(transactions):
    total_income = 0
    total_expenses = 0

    for transaction in transactions:

        if transaction["type"] == "income":
            total_income += transaction["amount"]

        elif transaction["type"] == "expense":
            total_expenses += transaction["amount"]

    balance = total_income - total_expenses

    print("\n========== BALANCE ==========")

    print(
        f"Total Income:   ₹{total_income:.2f}"
    )

    print(
        f"Total Expenses: ₹{total_expenses:.2f}"
    )

    print(
        f"Balance:        ₹{balance:.2f}"
    )


def category_summary(transactions):
    category_totals = {}

    for category in categories:
        category_totals[category] = 0

    for transaction in transactions:

        if transaction["type"] == "expense":

            category = transaction.get(
                "category",
                "Other"
            )

            amount = transaction["amount"]

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += amount

    print(
        "\n========== CATEGORY SUMMARY =========="
    )

    has_expenses = False

    for category, total in category_totals.items():

        if total > 0:
            print(
                f"{category}: ₹{total:.2f}"
            )

            has_expenses = True

    if not has_expenses:
        print("No expenses found.")