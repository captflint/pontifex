from pontifex import Deck
import random

decks = []

deck = Deck()

while len(decks) < 2000000:
    decks.append(deck.cards)
    deck.nextNumber()

def test():
    
    random.seed()
    decks.append(deck.cards)
    random.shuffle(decks)

#test()

if deck.cards in decks:
    print('Cycle detected')
    print('Index is', decks.index(deck.cards))
    print('--------------')
    print(deck)

else:
    print('No cycle detected')
