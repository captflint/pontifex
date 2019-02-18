#!/usr/bin/env python3

from pontifex import Message, Deck
import argparse

des = "Encrypt or decrypt messages with the Solitaire algorithm"
parser = argparse.ArgumentParser(description=des)
decksource = parser.add_mutually_exclusive_group()
decksource.add_argument('-k', '--key',
        help='use a key rather than a saved deck file')
decksource.add_argument('-d', '--deck',
        help='filename of saved deck to use')
parser.add_argument('-o', '--output',
        help='filename to save output to')
deckmanagement = parser.add_mutually_exclusive_group()
deckmanagement.add_argument('-b', '--backup', action='store_true',
        help='save copy of deck before performing the current operation')
deckmanagement.add_argument('-c', '--create-deck', action='store_true',
        help='create a new deck')
parser.add_argument('-p', '--phonetic', action='store_true',
        help='output codegroups in phonetic alphabet')
parser.add_argument('-s', '--subtract', action='store_true',
        help='subtract, rather than add, keystream - use this to decrypt')
parser.add_argument('filename',
        help='filename of message to process or deck to create')
args = parser.parse_args()

if args.create_deck:
    deck = Deck()

    if args.key != None:
        deck.key(args.key)

    f = open(args.filename, 'w')
    f.write(str(deck))
    f.close()

elif args.deck == None and args.key == None:
    print("A saved deck file or key must be supplied.")

else:

    if args.deck:

        f = open(args.deck, 'r')
        deck = f.read()
        f.close()
        deck = Deck(deck)

    else:
        deck = Deck()
        deck.key(args.key)

    if args.backup:
        f = open(args.deck + '.old', 'w')
        f.write(str(deck))
        f.close()

    f = open(args.filename, 'r')
    message = f.read()
    message = Message(message)

    if args.subtract:
        message = deck.decrypt(message)

    else:
        message = deck.encrypt(message)

    if args.deck and '.old' not in args.deck:
        f = open(args.deck, 'w')
        f.write(str(deck))
        f.close()

    if args.phonetic:
        message = message.phonetic()

    else:
        message = str(message)

    if args.output:
        f = open(args.output, 'w')
        f.write(message + '\n')
        f.close()

    else:
        print(message)
