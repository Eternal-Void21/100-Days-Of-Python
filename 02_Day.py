print("Welcome to the Tip Calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? "))
people = int(input("How many people will split the bill? "))
amount_each = (total / people) * (1+(tip/100))
final = round(amount_each,2)
print(f"Each person should pay: ${final}")


