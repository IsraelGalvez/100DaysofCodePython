# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2
t = (names.lower()).count("t")
r = (names.lower()).count("r")
u = (names.lower()).count("u")
e = (names.lower()).count("e")

result_true = t + r + u + e

l = (names.lower()).count("l")
o = (names.lower()).count("o")
v = (names.lower()).count("v")
e = (names.lower()).count("e")

result_love = l + o + v + e

final_result = (result_true * 10) + result_love

if final_result < 10 or final_result > 90:
    print(f"Your score is {final_result}, you go together like coke and mentos.")
elif final_result >= 40 and final_result <= 50:
    print(f"Your score is {final_result}, you are alright together.")
else:
    print(f"Your score is {final_result}.")