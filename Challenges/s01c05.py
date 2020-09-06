import math

def repeating_key_XOR(pt, k):
    ct = b''
    for i, j in zip(pt, k):
        ct+=bytes([i ^ j])
    return ct

def main():
    plaintext = b'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
    key = b'ICE'
    new_key = key * (math.ceil(len(plaintext) / len(key)))
    ciphertext = repeating_key_XOR(plaintext, new_key)
    print(ciphertext.hex())

if __name__ == '__main__':
    main()
