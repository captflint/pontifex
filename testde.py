import pontifex

f = open('test.deck', 'r')
d = f.read()
f.close()
d = pontifex.Deck(d)

print('reading')
f = open('encrypted.txt', 'r')
pandp = f.read()
f.close()
pandp = pontifex.Message(pandp)

print('decrypting')
pandp = d.decrypt(pandp)

print('writing')
f = open('decrypted.txt', 'w')
f.write(str(pandp))
f.close()
