import sqlite3
from datetime import datetime


conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    date TEXT,
    type TEXT,
    category TEXT,
    description TEXT,
    amount REAL
)
''')
conn.commit()

def add_transaction():
    date = input("Enter the date (YYYY-MM-DD): ")
    t_type = input("Enter type (Income/Expense): ")
    category = input("Enter category (e.g., Food, Rent): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    cursor.execute('''
    INSERT INTO transactions (date, type, category, description, amount)
    VALUES (?, ?, ?, ?, ?)
    ''', (date, t_type, category, description, amount))
    conn.commit()
    print("Transaction added successfully!")

def view_transactions():
    print("Viewing all transactions:")
    cursor.execute('SELECT * FROM transactions')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def calculate_balance():
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Income'")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='Expense'")
    expense = cursor.fetchone()[0] or 0

    balance = income - expense
    print(f"Total Income: {income}, Total Expense: {expense}, Balance: {balance}")

def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Calculate Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            calculate_balance()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
