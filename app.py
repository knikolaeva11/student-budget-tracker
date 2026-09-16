print("Welcome to the Student Budget Tracker")

budget = float(input("What is your monthly budget?"))

expense = float(input("How much did you spend? "))
remaining = budget - expense

print(f"You have £{remaining:.2f} remaining!")
