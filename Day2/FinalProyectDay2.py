print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill?"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
numPeople = int(input("How many people to split the bill?"))
result = (totalBill*(1+(percentage/100))) / numPeople
print(f"Each person should pay: ${round(result,2)}")