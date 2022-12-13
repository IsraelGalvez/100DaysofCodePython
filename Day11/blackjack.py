import random
from art import logo

cards_random = [1,2,3,4,5,6,7,8,9,10,10,10,10]

def continue_game():
    play_boolean = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    return play_boolean

def winner(user,computer):
    winner = ""
    sum_user = sum_list(user)
    
    sum_computer = sum_list(computer)
    
    if sum_user > sum_computer and sum_user < 22:
        winner = "You win"
    elif sum_computer > sum_user and sum_computer < 22:
        winner = "You lose"
    elif sum_computer > 21 and sum_user < 22:
        winner = "You win"
    elif sum_computer == sum_user and sum_computer < 22:
        winner = "draw"
    else:
        winner = "You lose"

    return str(winner)

def sum_list(list):
    sum_of_cards = 0
    for num in list:
        sum_of_cards += num
    return sum_of_cards

def add_new_cards(cards, yes_or_not):
    list = []
    sum_of_cards = sum_list(cards)
    for card in cards:
        if (card == 1 and (sum_of_cards + 10) < 22):
            list.append(11)
            if cards[0] == 1:
                sum_of_cards += 10
        else:
            list.append(card)
        
    sum_of_cards = sum_list(list)

    count = 0
    while(sum_of_cards < 17 and yes_or_not == "y"):
        count += 1
        if sum_of_cards < 17:
            if count == 1:
                list.append((random.choice(cards_random)))
            else:
                yes_or_not = input("Type 'y' to get another card, type 'n' to pass: ")
                print(list)
                if yes_or_not == "y":
                    list.append((random.choice(cards_random)))
            if list[0] != 11 and list[1] != 11 and list[2] == 1 and (sum_of_cards+10) < 22:
                list[2] = 11
            sum_of_cards = sum_list(list)
    
    return list

Should_continue = True

def blackjack_game():
    global Should_continue 
    petition_to_play = continue_game()
    if petition_to_play == 'n':
        Should_continue = False 

    print(logo)

    while Should_continue:
        user_winner = ""

        user_cards = [
            random.choice(cards_random), 
            random.choice(cards_random)]

        computer_cards = [
            random.choice(cards_random), 
            random.choice(cards_random)]

        print(f"Your cards: {user_cards}")
        print(f"Computer's first card: {computer_cards[0]}")

        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        user_cards = add_new_cards(user_cards, another_card)

        computer_sum_card = sum_list(computer_cards)
        if computer_sum_card < 17:
            computer_cards = add_new_cards(computer_cards, "y")

        print(f"Your final hand: {user_cards}")
        print(f"Computer's final hand: {computer_cards}")

        user_winner = winner(user_cards, computer_cards)
        print(user_winner)
        blackjack_game()

blackjack_game()