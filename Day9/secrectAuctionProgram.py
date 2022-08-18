people = {}

def secrectAuction():
    run = True
    while run:
        name = input("What is your name?: ")
        bid = float(input("What's your bid?: $"))
        
        people[name] = bid
        another_person = input("Are there any other bidders? Type 'yes or 'no'.")
        if another_person == "no":
            run = False
    winner = winner(people)
    bid = people[winner]
    print("The winner is James with a bid of $" + bid)
            
def winner(people):
    num = 1
    winner = ""
    for person in people:
        if num == 1:
            winner = person
            num = 2
        elif people[person] > people[winner]:
            winner = person
    return winner
        