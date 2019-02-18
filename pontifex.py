import random
random.seed()

class Message:

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, data=[]):

        self.numbers = []

        if type(data) is Message:
            data = data.numbers

        if type(data) is list:
            
            for n in data:

                if type(n) is int and n >= 1 and n <= 26:
                    self.numbers.append(n)

        if type(data) is str:

            data = data.upper()

            for l in data:

                if l in self.alphabet:
                    self.numbers.append(self.alphabet.index(l) + 1)

        while len(self.numbers) % 5 != 0:
            self.numbers.append(self.alphabet.index('X') + 1)

    def __eq__(self, other):

        if type(other) is Message:
            return(self.numbers == other.numbers)

        else:
            return(False)

    def letters(self):

        letters = ""

        for n in self.numbers:
            letters += self.alphabet[n - 1]

        return(letters)

    def __str__(self):

        returnString = ""
        counter = 0

        for l in self.letters():
            returnString += l
            counter += 1

            if counter == 50:
                returnString += '\n\n'
                counter = 0

            if counter % 5 == 0 and counter > 0:
                returnString += ' '

        return(returnString)

    def __repr__(self):

        returnString = '"""\n'
        returnString += str(self)
        returnString += '\n"""\n'
        return(returnString)

    def phonetic(self):

        returnString = ""
        counter = 0
        phonetic = [
                'Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
                'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima',
                'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo',
                'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey',
                'X-ray', 'Yankee', 'Zulu' ]

        for n in self.numbers:
            returnString += phonetic[n - 1]
            counter += 1

            if counter == 5:
                returnString += '\n'
                counter = 0

            else:
                returnString += ' '

        returnString += '\n'
        return(returnString)

class Deck:

    def shuffle(self):

        self.cards = []

        for i in range(1, 55):
            self.cards.append(i)
            random.shuffle(self.cards)

    def check(self):

        if len(self.cards) != 54:
            self.shuffle()
            return()

        for c in self.cards:
            
            if type(c) is int:
                pass
            
            else:
                self.shuffle()
                return()

        for i in range(1, 55):

            if i in self.cards:
                pass

            else:
                self.shuffle()
                return()

    def __init__(self, cardlist=None):

        self.shuffle()

        if cardlist and type(cardlist) is list:
            self.cards = cardlist
            self.check()

        if cardlist and type(cardlist) is Deck:
            self.cards = cardlist.cards
            self.check()

        if cardlist and type(cardlist) is str:

            cardlist += ' '
            self.cards = []
            cardWords = []
            cardWord = ""
            validValues = [
                    'A', '2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'J', 'Q', 'K' ]

            cardlist = cardlist.upper()

            for c in cardlist:

                if c in '\n\t ':
                    
                    if cardWord:
                        cardWords.append(cardWord)
                        cardWord = ""

                else:
                    cardWord += c

            for word in cardWords:
                suit = word[-1]
                value = word[:-1]

                if suit in 'CDHSJ':
                    suit = 'CDHSJ'.index(suit) * 13

                else:
                    continue

                if value == '1':
                    value = 'A'

                if value in validValues:
                    value = validValues.index(value) + 1

                else:
                    continue

                self.cards.append(value + suit)

            self.check()

    def step1(self):

        newcards = []

        if self.cards[-1] == 53:
            newcards.append(self.cards[0])
            newcards.append(53)

            for c in self.cards[1:]:

                if c != 53:
                    newcards.append(c)

            self.cards = newcards

        else:

            jokerIsNext = False

            for c in self.cards:

                if jokerIsNext:
                    newcards.append(c)
                    newcards.append(53)
                    jokerIsNext = False

                else:

                    if c == 53:
                        jokerIsNext = True

                    else:
                        newcards.append(c)

                self.cards = newcards

    def step2(self):

        newcards = []

        if 54 in self.cards[-2:]:

            if self.cards[-1] == 54:
                newcards = self.cards[:2]
                i = 2

            else:
                newcards.append(self.cards[0])
                i = 1

            newcards.append(54)

            for c in self.cards[i:]:

                if c != 54:
                    newcards.append(c)

        else:

            joker = 0

            for c in self.cards:

                if joker:

                    if joker == 2:
                        newcards.append(c)
                        joker = 1

                    else:
                        newcards.append(c)
                        newcards.append(54)
                        joker = 0

                else:
                    
                    if c == 54:
                        joker = 2

                    else:
                        newcards.append(c)

        self.cards = newcards

    def step3(self):

        start = []
        middle = []
        end = []
        state = 's'

        for c in self.cards:

            if state == 's':

                if c > 52:
                    state = 'm'
                    middle.append(c)

                else:
                    start.append(c)

            elif state == 'm':
                middle.append(c)

                if c > 52:
                    state = 'e'

            else:
                end.append(c)

        self.cards = end + middle + start

    def step4(self):

        bottom = self.cards[-1]
        rest = self.cards[:-1]

        i = bottom
        if i == 54:
            i = 53

        upper = rest[:i]
        lower = rest[i:]

        self.cards = lower + upper + [bottom]

    def outputCard(self):

        self.step1()
        self.step2()
        self.step3()
        self.step4()

        i = self.cards[0]
        if i == 54:
            i = 53

        return(self.cards[i])

    def nextNumber(self):

        card = 100

        while card > 52:
            card = self.outputCard()

        if card > 26:
            card -= 26

        return(card)

    def key(self, k):

        self.cards.sort()

        if type(k) is str:
            k = k.upper()
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            for c in k:

                if c in alphabet:
                    self.step1()
                    self.step2()
                    self.step3()
                    self.step4()

                    i = alphabet.index(c) + 1
                    bottom = self.cards[-1]
                    rest = self.cards[:-1]
                    upper = rest[:i]
                    lower = rest[i:]

                    self.cards = lower + upper + [bottom]

    def encrypt(self, message):

        if type(message) is Message:
            out = []

            for n in message.numbers:
                n += self.nextNumber()

                if n > 26:
                    n -= 26

                out.append(n)

            return(Message(out))

        else:
            return(Message())

    def decrypt(self, message):

        if type(message) is Message:
            out = []

            for n in message.numbers:
                n -= self.nextNumber()

                if n < 1:
                    n += 26

                out.append(n)

            return(Message(out))

        else:
            return(Message())

    def __str__(self):

        returnString = ""
        counter = 0

        for c in self.cards:

            if c < 53:

                suit = 0

                while c > 13:
                    c -= 13
                    suit += 1

                if c < 11:
                    returnCard = str(c)

                    if returnCard == '1':
                        returnCard = 'A'

                else:
                    c -= 11
                    returnCard = 'JQK'[c]

                returnCard += 'CDHS'[suit]
                returnString += returnCard

            if c == 53:
                returnString += '1J'

            if c == 54:
                returnString += '2J'

            counter += 1
            
            if counter == 5:
                returnString += '\n'
                counter = 0

            else:
                returnString += ' '

        return(returnString + '\n')

    def __repr__(self):
        
        return('"""\n' + str(self) + '\n"""\n')
