#!/usr/bin/python3

import string
import binascii

#concept 
#1) map A-Z to 1-26
#2) get the character & mapping number->character
#3) convert to ascii

#generate 1-26 with a-z in dictionary
alphanumMap = dict(zip(range(1,27), string.ascii_lowercase))

#from challenge image extracted numbers
chal = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }".split()

#print flag
print("FLAG: ", end="")
for x in chal:
	if(x.isdigit()):		
		print(alphanumMap[int(x)].upper(), end="")
	else:
		print(x, end="")