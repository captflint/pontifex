import argparse, pontifex

actions = [
        'encrypt',
        'decrypt',
        'shuffle',
        'phonetic',
        'write' ]

parser = argparse.ArgumentParser('clipontifex.py')
parser.add_argument('action', choices=actions, help="action to perform")
parser.add_argument('-d', '--deck', nargs='?', default='default.dec')
parser.add_argument('-m', '--message', nargs='?', default='message.txt')
parser.add_argument('-b', '--backup', action='store_true', help='Save old deck')
args = parser.parse_args()

def openDeck():

    f = open(args.deck, 'r')
    d = f.read()
    f.close()
    d = pontifex.Deck(d)
    return(d)

def saveDeck(d):

    if args.backup:
        backup = openDeck()
        f = open(args.deck + '.old', 'w')
        f.write(str(backup))
        f.close()

    f = open(args.deck, 'w')
    f.write(str(d))
    f.close()

def openMessage():

    f = open(args.message, 'r')
    m = f.read()
    f.close()
    m = pontifex.Message(m)
    return(m)

def saveMessage(m):

    f = open(args.message, 'w')
    f.write(str(m) + '\n')
    f.close()

def openBoth():

    d = openDeck()
    m = openMessage()
    return(d, m)

def saveBoth(d, m):

    saveDeck(d)
    saveMessage(m)

def encrypt():

    deck, message = openBoth()
    message = deck.encrypt(message)
    saveBoth(deck, message)

def decrypt():

    deck, message = openBoth()
    message = deck.decrypt(message)
    saveBoth(deck, message)

def shuffle():

    deck = pontifex.Deck()
    saveDeck(deck)

def phonetic():

    message = openMessage()
    print(message.phonetic())

def write():

    deck = openDeck()
    message = input("Type you message and press enter to encrypt.\n> ")
    message = pontifex.Message(message)
    message = deck.encrypt(message)
    print(message)
    saveBoth(deck, message)

actiondict = {
        'encrypt': encrypt,
        'decrypt': decrypt,
        'shuffle': shuffle,
        'phonetic': phonetic,
        'write': write
        }

a = actiondict[args.action]
a()
