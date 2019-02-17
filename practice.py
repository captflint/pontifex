from pontifex import Deck

deck = Deck()

print('Your deck order is:')
print(deck)
input('Press enter to continue.')

cont = True
score = 0

def filterGuess(g):

    r = ''

    for c in g:

        if c in '1234567890':
            r += c

    if len(r):
        r = int(r)
        return(r)

    else:
        return(0)

while cont:
    answer = deck.nextNumber()
    print('\n\n\nScore:', score)
    guess = input('What is the next number? ')
    guess = filterGuess(guess)
    cont = answer == guess
    
    if cont:
        print('Correct')
        score += 1

    else:
        print('Incorrect')
        print('Your final score:', score)
