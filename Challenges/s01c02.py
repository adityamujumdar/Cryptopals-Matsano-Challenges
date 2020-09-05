def fixed_xor(buf1,buf2):
    if(len(buf1) == len(buf2)):
        # int converts the buffers to base 16 (for hexadecimal numbers) and xors. hex() converts to hex string for display
        return hex(int(buf1,16)^(int(buf2,16)))

plaintext_hex = fixed_xor('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965')
print(plaintext_hex)
