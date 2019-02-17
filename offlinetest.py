import pontifex

f = open('default.dec', 'r')
deck = f.read()
f.close()
deck = pontifex.Deck(deck)

print("Step 1 - Please input a short message and then press enter.\n")
message = input('> ')
message = pontifex.Message(message)
message = deck.encrypt(message)

print('\n' * 200)
print("Step 2 - Please read the following words and then press enter.\n")
print(message.phonetic())
input()

print("Step 3 - Please close laptop. Thanks <3")
