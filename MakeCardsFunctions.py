# cards

suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades'] #suit types
cardno = ['2', '3','4','5','6','7','8','9','10','J','Q','K','A'] # card numbers

def make_cards():
    cards = [] # Empty to start
    for s in suits: # List suits
        for i in cardno:  # list card numbers in suit.
            cards.append(i+'-'+s)
    return cards
my_cards = make_cards()
print(my_cards)

input('Press enter to exit')
