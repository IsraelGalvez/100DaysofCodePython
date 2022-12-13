from art import vs, logo
from game_data import data
import random

def print_logo():
    print(logo)

def print_vs():
    print(vs)

def load_data(data, num):
    dictionary = data
    name = dictionary['name']
    description = dictionary['description']
    country = dictionary['country']
    follower_count = dictionary['follower_count']

    if num == 1:
        print(f"Compare A: {name}, a {description}, from {country}")
    else:
        print(f"Against B: {name}, a {description}, from {country}")
    
    return follower_count

def calculate_result(option1, option2, answer):
    if option1 > option2 and answer == 'A':
        return "right_answer"
    elif option1 == option2:
        return "right_answer"
    elif option2 > option1 and answer == 'B':
        return "right_answer"
    else:
        return"wrong_answer"

def counter(number, result):
    if result == "right_answer":
        number += 1
    return number

def main():
    answer = "right_answer"
    counter_num = 0
    num = 1
    while answer == "right_answer":
        data1 = random.choice(data)
        data2 =random.choice(data)
        if data1 == data2:
            data2 =random.choice(data)
        print_logo()
        if num > 1:
            print(f"You're right! Current score: {counter_num}")
        option1 = load_data(data1, 1)
        print_vs()
        option2 = load_data(data2, 2)
        choise_option = input("Who has more followers? Type 'A' or 'B': ").upper()
        result = calculate_result(option1, option2, choise_option)
        counter_num = counter(counter_num, result)
        answer = result
        num +=1
    print(f"Sorry, that's wrong. Final score: {counter_num}")
    


main()

