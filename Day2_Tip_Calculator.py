print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
total = (total * (1 + (tip / 100)))
people = int(input("How many people to split the bill? "))
each = round(total / people, 2)
each = "{:.2f}".format(each) # f strings help with formatting and rounding to exact place
print(f"Each person should pay: ${each}" )
