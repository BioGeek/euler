# based on: http://www.evanfosmark.com/2008/06/xor-encryption-with-python/ 

from itertools import izip, cycle, combinations_with_replacement
from string import lowercase

with open('cipher1.txt') as f:
    data = [int(i) for i in f.read().strip().split(',')]

decrypted = dict()

# for key in (''.join(i) for i in combinations_with_replacement(lowercase, 3)):
#    decrypted[key] = ''.join(chr(int(i) ^ ord(y))  for (i,y) in izip(data.strip().split(','),cycle(key)))

def encrypt(data, key): #data is a string
    return [ord(x)^ord(y) for (x,y) in izip(data,cycle(key))]

def decrypt(data, key): # data is a list of ints
    return ''.join(chr(x^ord(y)) for (x,y) in izip(data,cycle(key)))
    

# for key in (''.join(i) for i in combinations_with_replacement(lowercase, 3)):   <== WRONG!!
for key in [a+b+c for a in lowercase for b in lowercase for c in lowercase]:
    decrypted[key] = decrypt(data, key)
    
solution = [v for k,v in decrypted.items() if ' the ' in v]

print sum(ord(i) for i in solution[0])

"""    
decrypted_freqs = dict()   
for key, text in decrypted.items():
    d = defaultdict(int)
    for letter in text:
        d[letter] += 1
    decrypted_freqs[key] = d
"""    

"""
def xor_crypt_string(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    
my_data = "Hello. This is a secret message! How fun."
my_key= "firefly"
 
# Do the actual encryption
encrypted = xor_crypt_string(my_data, key=my_key)
print encrypted
 
# This will obtain the original data from the encrypted
original = xor_crypt_string(encrypted, key=my_key)
"""
