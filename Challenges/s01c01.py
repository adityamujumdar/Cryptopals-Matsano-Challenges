from base64 import b64encode, b64decode
ciphertext = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
ciphertext_bytes = bytes.fromhex(ciphertext)
print(ciphertext_bytes, b64encode(ciphertext_bytes).decode())
