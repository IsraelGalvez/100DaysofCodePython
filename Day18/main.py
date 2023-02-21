import random

cards = { "espada": [1,2,3,4,5,6,7,8,9,10,"J","Q","K"], 
          "diamante": [1,2,3,4,5,6,7,8,9,10,"J","Q","K"], 
          "corazon": [1,2,3,4,5,6,7,8,9,10,"J","Q","K"], 
          "trebol": [1,2,3,4,5,6,7,8,9,10,"J","Q","K"],
        }


user_cards = {}
computer_cards = {}

def get_random_cards(all_cards, five_cards):
    list_espadas = []
    list_diamantes = []
    list_corazones = []
    list_treboles = [] 
    for num in range(0,5):
        type_of_card = random.choice(list(all_cards))
        value_of_card = random.choice(list(all_cards[type_of_card]))
        if type_of_card == "espada":
            list_espadas.append(value_of_card)
        elif type_of_card == "diamante":
            list_diamantes.append(value_of_card)
        elif type_of_card == "corazon":
            list_corazones.append(value_of_card)
        elif type_of_card == "trebol":
            list_treboles.append(value_of_card)
        value_of_dictionary = all_cards[type_of_card]
        value_card_index = value_of_dictionary.index(value_of_card)
        value_of_dictionary.pop(value_card_index)
        if type_of_card == "espada":
            five_cards[type_of_card] = list_espadas
        elif type_of_card == "diamante":
            five_cards[type_of_card] = list_diamantes
        elif type_of_card == "corazon":
            five_cards[type_of_card] = list_corazones
        elif type_of_card == "trebol":
            five_cards[type_of_card] = list_treboles
        all_cards[type_of_card] = value_of_dictionary

def sum_cards(five_cards):
    list_of_type_of_cards = list(five_cards.keys())
    list_of_list = []
    for type in list_of_type_of_cards:
        list_of_list.append(five_cards[type])
    list_of_values = []
    for sublist in list_of_list:
        for item in sublist:
            list_of_values.append(item)
    count = 0
    for item in list_of_values:
        list_of_values[count] = str(item)
        count += 1
    list_of_values.sort()
    print(list_of_values)
    par_tercia_full(list_of_values)
    print("hola")

def par_tercia_full(list_of_value_of_the_cards):
    length = len(list_of_value_of_the_cards)
    count = 0
    score = 0
    for num in range(5):
        list_of_value_of_the_cards.append(0)
    while count < length:
        if list_of_value_of_the_cards[count] == list_of_value_of_the_cards[count+1]:
            if list_of_value_of_the_cards[count] == list_of_value_of_the_cards[count+2]:
                if list_of_value_of_the_cards[count] == list_of_value_of_the_cards[count+3]:
                    if list_of_value_of_the_cards[count] == "J" or list_of_value_of_the_cards[count] == "Q" or list_of_value_of_the_cards[count] == "K":
                        score += 10 * 4 * 4
                        count += 4
                    else:
                        score += int(list_of_value_of_the_cards[count]) * 4 * 4
                        count += 4
                else:
                    if list_of_value_of_the_cards[count] == "J" or list_of_value_of_the_cards[count] == "Q" or list_of_value_of_the_cards[count] == "K":
                        score += 10 * 3 * 3
                        count += 3
                    else:
                        score += int(list_of_value_of_the_cards[count]) * 3 * 3
                        count += 3
            else:
                if list_of_value_of_the_cards[count] == "J" or list_of_value_of_the_cards[count] == "Q" or list_of_value_of_the_cards[count] == "K":
                        score += 10 * 2 * 2
                        count += 2
                else:
                    score += int(list_of_value_of_the_cards[count]) * 2 * 2
                    count += 2
        else:
            if list_of_value_of_the_cards[count] == "J" or list_of_value_of_the_cards[count] == "Q" or list_of_value_of_the_cards[count] == "K":
                score += 10
            else:
                score += int(list_of_value_of_the_cards[count])
                count += 1
    print(score)

def main():
    get_random_cards(cards, user_cards)
    get_random_cards(cards, computer_cards)
    print(user_cards)
    print(computer_cards)
    sum_cards(user_cards)

main()