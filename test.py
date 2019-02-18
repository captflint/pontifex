import pontifex

f = open('sol-test.txt', 'r')
soltest = f.read()
f.close()

tests = soltest.split('\n\n')

class Test:

    def run(self):

        deck = pontifex.Deck()
        deck.key(self.key)

        self.result = deck.encrypt(self.plain)
        self.passed = self.expected == self.result

    def __init__(self, s):

        s = s.splitlines()

        def processLine(lines, prefix):

            out = ""

            for line in lines:

                if line.startswith(prefix):
                    out = line.partition(prefix)
                    out = out[-1]
                    out = out.strip(" \t:'")

            return(out)

        self.plain = processLine(s, 'Plaintext')
        self.key = processLine(s, 'Key')
        self.expected = processLine(s, 'Ciphertext')

        self.plain = pontifex.Message(self.plain)

        if self.key == '<null key>':
            self.key = ''

        self.expected = pontifex.Message(self.expected)

        self.run()

    def __str__(self):

        rstring = ""
        rstring += 'Plaintext = "' + str(self.plain) + '"\n'
        rstring += 'Key = "' + self.key + '"\n'
        rstring += 'Expected result = "' + str(self.expected) + '"\n'
        rstring += 'Actual result = "' + str(self.result) + '"\n'
        rstring += 'Passed = ' + str(self.passed)

        return(rstring)

i = 0
cont = True
for t in tests:
    i += 1
    print('Test', i)
    t = Test(t)
    print(t)
    print()
    cont = t.passed
    if not cont:
        break
