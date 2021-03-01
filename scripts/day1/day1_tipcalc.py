print("Welcome to the tip calculator")
total = float(input("What was the total bill? £"))
people = int(input("How many people are splitting the bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?")) / 100
total_with_tip = (tip * total) + total
ind = round((total_with_tip / people), 2)
print(f"Each person owes ${ind}")