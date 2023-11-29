"""
File: caesar.py
Name: 許景涵
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_DICT = {"A": 1,  "B": 2,  "C": 3,  "D": 4,  "E": 5,  "F": 6,  "G": 7,  "H": 8, "I": 9,
                 "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
                 "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
# Give all alphabets its number of order


def main():
    """
    This program first asks users to enter a number that shifts ALPHABET to the right.
    After that, any strings typed in will be encrypted.
    Lastly it finds out the deciphered string.
    """
    secret = int(input('Secret number: '))
    ciphered = input("What's the ciphered string? ")
    ciphered = ciphered.upper()
    deciphered_word = decipher(secret, ciphered)
    print('The deciphered string is: ' + deciphered_word)


def decipher(secret, ciphered):
    shift = secret % 26   # The number ALPHABET shifts to the right compared with the original order
    ans = ''
    for ch in ciphered:
        index_ch = (ALPHABET_DICT[ch] + shift) % 26   # Gets the new index of the shifted alphabet
        ans += ALPHABET[index_ch - 1]   # Appends the deciphered character to the answer
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
