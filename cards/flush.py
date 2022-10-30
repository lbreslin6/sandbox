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

flush = [{'suit':'diamonds', 'number': 1},{'suit':'diamonds', 'number': 2},{'suit':'diamonds', 'number': 3},{'suit':'diamonds', 'number': 4},{'suit':'diamonds', 'number': 5}]

def is_hand_flush(hand):
    if (hand[0]['suit']==hand[1]['suit']==hand[2]['suit']==hand[3]['suit']==hand[4]['suit']):
        return True
    else: 
        return False

print (is_hand_flush(flush))

def flush_test(n):
    i = 0
    flush_count = 0
    while (i<n):
        if (is_hand_flush(pick_no_replacement(5, deck))):
            flush_count += 1
        i += 1
    return (flush_count/n*100)



print(f'{flush_test(100000000)}%')






