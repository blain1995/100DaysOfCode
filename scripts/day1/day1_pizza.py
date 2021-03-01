# Take pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Work out price
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
    if extra_cheese == "Y":
      bill += 1
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
    if extra_cheese == "Y":
      bill += 1
else:
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
    if extra_cheese == "Y":
      bill += 1

# Tell customer total price
print(f'Your final bill is £{bill}')