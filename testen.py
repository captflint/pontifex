import pontifex

d = pontifex.Deck()
f = open('test.deck', 'w')
f.write(str(d))
f.close

print('reading')
f = open('pandp.txt', 'r')
pandp = f.read()
f.close()
pandp = pontifex.Message(pandp)

print('encrypting')
pandp = d.encrypt(pandp)

print('writing')
f = open('encrypted.txt', 'w')
f.write(str(pandp))
f.close()
