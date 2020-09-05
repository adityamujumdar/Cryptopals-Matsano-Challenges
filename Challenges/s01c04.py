from s01c03 import get_bytewise_xor, get_character_frequency

def get_max_score_1(ciphertext_str: str) -> list:
    ciphertext = bytes.fromhex(ciphertext_str)
    plaintext = []
    for key in range(0,255):
        xord = get_bytewise_xor(ciphertext, key)
        frequency = get_character_frequency(xord)
        plaintext.append((frequency, key, xord))
    answer = sorted(plaintext, key=lambda x: x[0], reverse = True)
    ret_lst = [answer[k] if answer[k][0]>1 else 0 for k in range(0,5)]
    return (ret_lst[0])

def get_highest_scoring_bytestring(filename: str) -> list:
    ciphertext_lst = []
    with open(filename,'r') as data:
        datalines = (line.rstrip('\r\n') for line in data)
        for i in datalines:
            ciphertext_lst.append(i)
    for i in range(len(ciphertext_lst)):
        if (get_max_score_1(ciphertext_lst[i]) != 0):
            ans = get_max_score_1(ciphertext_lst[i])
    return ans[2]
        
def main():
    filename = 's01c04.txt'
    print(get_highest_scoring_bytestring(filename))
    
if __name__ == '__main__':
    main()
