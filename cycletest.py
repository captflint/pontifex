#!/usr/bin/env python3

from pontifex import Deck
import random, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--false-positive', action='store_true')
decksource = parser.add_mutually_exclusive_group()
decksource.add_argument('-k', '--key')
decksource.add_argument('-d', '--deck')
parser.add_argument('-l', '--length', type=int, default=1000000)
args = parser.parse_args()

print('Checking for cycles of length less than or equal to', args.length)

decks = []

deck = Deck()

if args.deck:
    f = open(args.deck, 'r')
    deck = Deck(f.read())
    f.close()

if type(args.key) is str:
    deck.key(args.key)

while len(decks) < args.length:
    decks.append(deck.cards)
    deck.nextNumber()

def false_positive():
    
    random.seed()
    decks.append(deck.cards)
    random.shuffle(decks)

if args.false_positive:
    false_positive()

if deck.cards in decks:
    print('Cycle detected')
    print('Index is', decks.index(deck.cards))
    print('--------------')
    print(deck)

else:
    print('No cycle detected')
