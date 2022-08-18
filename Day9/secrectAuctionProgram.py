import art
import os

people = {}
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def secrectAuction():
    run = True
    print(art.logo)
    while run:
        name = input("What is your name?: ")
        bid = float(input("What's your bid?: $"))
        
        people[name] = bid
        another_person = input("Are there any other bidders? Type 'yes or 'no'.").lower()
        if another_person != "yes":
            run = False
        clearConsole()
    winner = winnerPerson(people)
    bid = people[winner]
    if bid > 0:
        print(f"The winner is {winner} with a bid of ${bid}")
    else:
        print("No one win")
            
def winnerPerson(people):
    num = 1
    winner = ""
    for person in people:
        if num == 1:
            winner = person
            num = 2
        elif people[person] > people[winner]:
            winner = person
    return winner

secrectAuction()
        