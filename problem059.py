# Each character on a computer is assigned a unique code and the preferred 
# standard is ASCII (American Standard Code for Information Interchange). For 
# example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, 
# then XOR each byte with a given value, taken from a secret key. The advantage 
# with the XOR function is that using the same encryption key on the cipher text, 
# restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, 
# and the key is made up of random bytes. The user would keep the encrypted message 
# and the encryption key in different locations, and without both "halves", it is 
# impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method 
# is to use a password as a key. If the password is shorter than the message, which 
# is likely, the key is repeated cyclically throughout the message. The balance 
# for this method is using a sufficiently long password key for security, but 
# short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower 
# case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), 
# a file containing the encrypted ASCII codes, and the knowledge that the plain 
# text must contain common English words, decrypt the message and find the sum of 
# the ASCII values in the original text.

# solution based on: http://www.evanfosmark.com/2008/06/xor-encryption-with-python/ 

from itertools import izip, cycle, combinations_with_replacement
from string import lowercase

with open('data/cipher1.txt') as f:
    data = [int(i) for i in f.read().strip().split(',')]

def encrypt(data, key): #data is a string
    return [ord(x)^ord(y) for (x,y) in izip(data,cycle(key))]

def decrypt(data, key): # data is a list of ints
    return ''.join(chr(x^ord(y)) for (x,y) in izip(data,cycle(key)))

# Check for sample values:
assert encrypt('A', '*')  == [107]
assert decrypt([107],'*') == 'A'

decrypted = {}

# decrypt the text for every lowercase three letter combination
# for key in (''.join(i) for i in combinations_with_replacement(lowercase, 3)):   <== WRONG!!
for key in [a+b+c for a in lowercase for b in lowercase for c in lowercase]:
    decrypted[key] = decrypt(data, key)

# check for common english word in decrypted text    
solution = [v for k,v in decrypted.items() if ' the ' in v]

# the encryption key is 'god'
# the decrypted text is: 
# (The Gospel of John, chapter 1) 1 In the beginning the Word already existed. 
# He was with God, and he was God. 2 He was in the beginning with God. 3 He 
# created everything there is. Nothing exists that he didn't make. 4 Life itself 
# was in him, and this life gives light to everyone. 5 The light shines through 
# the darkness, and the darkness can never extinguish it. 6 God sent John the 
# Baptist 7 to tell everyone about the light so that everyone might believe 
# because of his testimony. 8 John himself was not the light; he was only a 
# witness to the light. 9 The one who is the true light, who gives light to 
# everyone, was going to come into the world. 10 But although the world was 
# made through him, the world didn't recognize him when he came. 11 Even in his 
# own land and among his own people, he was not accepted. 12 But to all who 
# believed him and accepted him, he gave the right to become children of God. 
# 13 They are reborn! This is not a physical birth resulting from human passion 
# or plan, this rebirth comes from God.14 So the Word became human and lived 
# here on earth among us. He was full of unfailing love and faithfulness. And we 
# have seen his glory, the glory of the only Son of the Father.

print sum(ord(i) for i in solution[0])

# 107359
#
# real	0m8.032s
# user	0m7.890s
# sys	0m0.070s

