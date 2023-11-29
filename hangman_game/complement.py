"""
File: complement.py
Name: 許景涵
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program finds the complement strand of a DNA sequence given from the user.
    """
    dna = input("please give me a DNA strand and I'll find the complement: ")
    if dna != 'a''T''t''T''c''C''g''G':
        dna = input("please give me a DNA strand and I'll find the complement: ")
    dna = dna.upper()
    ans = build_complement(dna)
    print('The complement of ' + str(dna) + ' is ' + ans)


def build_complement(dna):
    """
    This program returns the complement dna
    """
    ans = ""
    for ch in dna:
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'C':
            ans += 'G'
        elif ch == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
