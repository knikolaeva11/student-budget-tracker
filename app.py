print("Welcome to the Student Budget Tracker! ")
print("Enter an expense or (0 to finsh)")
budget = float(input("What is your monthly budget?"))

total_expenses = 0

while True:

    expense = float(input("What is your expense?"))
    
    if expense == 0: 
        break
    total_expenses = total_expenses + expense

remaining = budget - total_expenses

print(f"Total Spent: £{total_expenses:.2f}")
      
if remaining >0:
    print(f"You have £{remaining:.2f} remaining!")
elif remaining == 0:
    print(f"You used your monthly budget")
else:
    print(f"You went over your budget by £{abs(remaining):.2f}")
