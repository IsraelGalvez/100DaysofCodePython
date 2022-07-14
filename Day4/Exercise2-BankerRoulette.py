import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

list_name = names
random_num = random.randint(0,len(list_name)-1)

print(f"{list_name[random_num]} is going to buy the meal today!")