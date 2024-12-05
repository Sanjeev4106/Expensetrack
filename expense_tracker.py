
import sqlite3
from datetime import datetime

# Initialize the database
def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Add a new expense
def add_expense(amount, category, description):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    ''', (amount, category, description, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

# View all expenses
def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Main CLI
def main():
    init_db()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., food, transport): ")
            description = input("Enter description: ")
            add_expense(amount, category, description)
            print("Expense added!")
        elif choice == '2':
            expenses = view_expenses()
            for expense in expenses:
                print(f"{expense[1]} | {expense[2]} | {expense[3]} | {expense[4]}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
