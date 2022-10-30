import random
deck = []
suits = ["spades", "clubs", "diamonds", "hearts"]
numbers = list(range(1,14))
for exsuit in suits:
    for exnumber in numbers:
        deck.append({'suit':exsuit,'number':exnumber})

def pick_no_replacement(n, init_deck):
    hand = []
    working_deck = init_deck.copy()
    for value in range(0,n):
        choice = random.randrange(0,len(working_deck))
        hand.insert(0, working_deck.pop(choice))
    return(hand)
print(pick_no_replacement(5,deck))
    



