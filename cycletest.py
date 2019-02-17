from pontifex import Deck

decks = []

def check4dups(deck):

    if deck.cards in decks:
        print("CYCLE FOUND!!!\n" * 10)
        print(str(deck))
        print('index', decks.index(deck.cards))
        f = open('cyclefound.dec', 'w')
        f.write(str(deck))
        f.close()

    else:
        decks.append(deck.cards)

deck = Deck()

while len(decks) < 1000000:
    check4dups(deck)
    n = deck.nextNumber()
    l = len(decks)
    if l % 1000 == 0:
        print(l, n)
