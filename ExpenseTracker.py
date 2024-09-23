import os

Expense_File = "expenses.txt"

def add_expense():
    date = input("Enter the date (DD_MM_YYYY) : ")
    category = input("Enter the category (e.g., Food, Travel, Entertainment): ")
    description = input("Enter the description : ")
    amount = float(input("Enter the amount : "))

    expense = f"{date},{category},{description},{amount}\n"

    # Save the expense to file
    with open(Expense_File, 'a') as file:
        file.write(expense)

    print("Expense added successfully")


def view_expense():
    if not os.path.exists(Expense_File):
        print("No expense found")
        return
    
    with open(Expense_File, 'r') as file:
        print(f"Date        | Category      | Description        | Amount")
        print("-"*50)
        for line in file:
            date, category, description, amount = line.strip().split(",")
            print(f"{date}   | {category:10}  | {description:15} | Rs.{amount}")


def view_expense_by_category():
    if not os.path.exists(Expense_File):
        print("No expense found")
        return
    
    category_filter = input("Enter the category to filter by: ")
    total = 0  # Initialize total
    
    with open(Expense_File, 'r') as file:
        print(f"Date       | Category       | Description        | Amount")
        print("-" * 50)
        for line in file:
            date, category, description, amount = line.strip().split(",")
            if category.lower() == category_filter.lower():
                print(f"{date}   | {category:10}  | {description:15} | Rs.{amount}")
                total += float(amount)

    print(f"\nTotal spent on {category_filter}: Rs.{total}")


def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View all Expenses")
        print("3. View Expense by category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            view_expense_by_category()
        elif choice == "4":
            print("Exiting the expense tracker")
            break  # Exit the loop
        else:
            print("Invalid choice, please enter a number between 1 and 4")


# Run the program
main()
