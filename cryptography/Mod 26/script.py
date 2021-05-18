import codecs

chal = """cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"""

#convert the ciphertext to plaintext with ROT13 
flag = codecs.encode(chal, "rot13")

print("FLAG: " + flag)