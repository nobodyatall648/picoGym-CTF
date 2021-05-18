#!/usr/bin/python3
import string

# grab from ciphertext (the text inside picoCTF{...} flag)
chal = 'ynkooejcpdanqxeykjrbdofgkq'

#generate 1-26 with a-z in dictionary
alphanumMap = dict(zip(string.ascii_lowercase, range(26)))

#getting the key from value 
def getKey(item):
    for key, value in alphanumMap.items():
        if(value == item):
            return key
    
    return 'Key not found!'

#perform brute forcing on 1-26 keys
print("[*] Find the flag that contain actual english words, that's the key to decrypt it!")
for key in range(26):    
    flag = ''    
    for char in chal:
        shifted = (key + alphanumMap[char]) % 26    #caesar cipher formula
        flag += getKey(shifted)

    print(str(key) + " : " + "picoCTF{" + flag + "}")



