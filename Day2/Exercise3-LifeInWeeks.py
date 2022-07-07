# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

daysLeft = (90*365) - (age*365)
weeksLeft = (90*52) - (age*52)
monthsLeft = (90*12) - (age*12)

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")