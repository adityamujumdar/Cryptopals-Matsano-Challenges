def get_bytewise_xor(text: bytes, key: int) -> bytes:
    return bytes([byte ^ key for byte in text])

def get_character_frequency(ciphertext: bytes):
    # Referenced from https://en.wikipedia.org/wiki/Letter_frequency
    character_frequencies = {
                    'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
                    'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
                    'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
                    'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
                    'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
                    'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
                    'y': .01974, 'z': .00074
    }
    frq = []
    for i in range(len(ciphertext.lower())):
        frq.append(character_frequencies.get(chr(ciphertext[i]),0))
    return sum(frq)

def main():
    hex_str_3 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ciphertext = bytes.fromhex(hex_str_3)
    plaintext = []
    for key in range(0,255):
        xord = get_bytewise_xor(ciphertext, key)
        frequency = get_character_frequency(xord)
        plaintext.append((frequency, key, xord))
    
    answer = sorted(plaintext, key=lambda x: x[0], reverse = True)
#     for k in range(0,5,1):
#         print(k, ':', answer[k])
    
    # key is 88
    print(answer[1][2])
        
if __name__ == '__main__':
    main()
