#!/usr/bin/python3

from Crypto.Util.number import *
import binascii

#cipertext
c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423

#n=p*q
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423

#public exponent (encryption key)
e = 65537

#to get p&q, need to perform integer factorizing
#since n is small, use website factordb.com to save time
#result => 	1311097532...23<82> = 1955175890537890492055221842734816092141<40> · 670577792467509699665091201633524389157003<42>
p = 1955175890537890492055221842734816092141
q = 670577792467509699665091201633524389157003

#finding phi(n)
phi = (p-1)*(q-1)

#find d (decryption key)
#formula: d = e^-1 mod phi(n)
#Cryptolib inverse(u, v) => inverse of u mod v
d = inverse(e, phi)

#finding p (plaintext)
#pow(4, 3, 5) ==>  4^3 mod 5 
p = pow(c, d, n)

#display flag
print("FLAG: " + long_to_bytes(p).decode())
