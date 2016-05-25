import binascii
import base64

def fixedXor(s):
    fixedString = '686974207468652062756c6c277320657965'
    return strxor(binascii.unhexlify(s), binascii.unhexlify(fixedString))

def strxor(s1,s2):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

test = '1c0111001f010100061a024b53535009181c'
ans = binascii.unhexlify('746865206b696420646f6e277420706c6179')
#print(test)
#print(ans)
if fixedXor(test) == ans:
    print("PASS")
else:
    print("FAIL")
