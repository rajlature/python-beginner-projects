
print("Welcome to the Tip Calculator!")

bill = 0
while bill <= 0:
    try:
        bill = float(input("Enter the total bill: ₹"))
        if bill <= 0:
            print("Please enter a positive bill amount.")
    except ValueError:
        print("Invalid input! Enter a number.")

tip = -1
while tip < 0:
    try:
        tip = float(input("Enter tip percentage: "))
        if tip < 0:
            print("Tip cannot be negative.")
    except ValueError:
        print("Invalid input! Enter a number.")

people = 0
while people <= 0:
    try:
        people = int(input("How many people? "))
        if people <= 0:
            print("Enter at least one person.")
    except ValueError:
        print("Invalid input! Enter a whole number.")

tip_amount = bill * tip / 100
total_amount = bill + tip_amount
per_person = total_amount / people

print(f"\nTip amount: ₹{tip_amount:.2f}")
print(f"Total bill: ₹{total_amount:.2f}")
print(f"Each person pays: ₹{per_person:.2f}")
