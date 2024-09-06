import json

from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = ["Food", "Transportation", "Entertainment", "Other"]
        self.load_expenses()

    def add_expense(self, amount, description, category):
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "amount": amount,
            "description": description,
            "category": category
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        for expense in self.expenses:
            print(f"{expense['date']} - {expense['category']} - ${expense['amount']} - {expense['description']}")

    def monthly_summary(self):
        # To be implemented
        pass

    def category_summary(self):
        # To be implemented
        pass

    def save_expenses(self):
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f)

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            self.expenses = []

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            print("Categories:", tracker.categories)
            category = input("Enter category: ")
            tracker.add_expense(amount, description, category)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.monthly_summary()
        elif choice == "4":
            tracker.category_summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()