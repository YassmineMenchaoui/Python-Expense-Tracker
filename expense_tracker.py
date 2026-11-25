
expenses = []

def add_expense():
    description = input("Expense description: ")
    amount = float(input("Expense amount: "))
    expenses.append({"description": description, "amount": amount})
    print("Expense added successfully.")

def show_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}. {expense['description']} - {expense['amount']:.2f}")

def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total expenses: {total:.2f}")

def show_average():
    if not expenses:
        print("No expenses recorded.")
    else:
        average = sum(item["amount"] for item in expenses) / len(expenses)
        print(f"Average expense: {average:.2f}")

def main():
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add an expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Exit")
        print("5. Show average")
        choice = input("Your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "5":
            show_average()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

main()
