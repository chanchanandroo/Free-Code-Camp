#Lambda Expense Tracker

This is a simple lambda expense tracker using Python lists and lambda functions. I followed the FreeCodeCamp instructions on how to build it. This is part of my self-learning journey in learning **Python**, **cybersecurity**, and **AI**. 

_ _ _ _ _
How to run this? 
Download the file and then run it using the terminal:

` ` ` bash
python lambda_expense_tracker.py


🎯 Why I Made This

I built this project mainly for my own learning.
But it might help someone else out there going through the FreeCodeCamp course too.

You can:

    Add expenses

    Filter by category

    View total expenses

    Exit the app

Each action is mapped to a lambda expression and shown as a button-like option.



🧠 Code Breakdown
add_expense(expenses, amount, category)

This function adds a new expense entry to the expenses list.
Each entry is stored as a dictionary with two keys: 'amount' and 'category'.
print_expenses(expenses)

Loops through the list of expenses and prints each one in a readable format.
Useful for displaying what the user has entered so far.
total_expenses(expenses)

Uses map() and a lambda function to extract the 'amount' from each entry, then sums them up.
This gives the total amount spent across all categories.
filter_expenses_by_category(expenses, category)

Uses filter() with a lambda to return only the expenses that match the specified category.
Good for seeing how much was spent in specific areas (e.g. "food", "transport").
main()

This is the core interactive loop of the app:

    Presents a menu to the user

    Asks for their choice

    Executes the correct function depending on that choice:

        Add an expense

        View all expenses

        See the total amount spent

        Filter expenses by category

        Exit the program


Example output: 

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit

Enter your choice: 


It loops until the user chooses to exit.

📌 Final Notes

Feel free to modify or expand the program!
It’s a great beginner-level tool to understand functional programming and lambda usage in real-world logic.


Code breakdown:

def add_expense(expenses, amount, category):  #def function and listing 3 parameters
    expenses.append({'amount': amount, 'category': category}) #listing out the key and face amount
    
def print_expenses(expenses): #looping expense function so that expense button always shows up
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}') # adds a dictionary for each category to expense list 
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:  #manually showing each button for user to see and choose
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1': #if enter choice 1, will ask user to enter an amount
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2': #enter choice 2, will show all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':  #choice 3 is sum of all expenses
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4': #choice 4 is input a category to filter
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5': # choice 5 is quit the program
            print('Exiting the program.')
            break