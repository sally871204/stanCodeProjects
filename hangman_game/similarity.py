"""
File: similarity.py
Name: 許景涵
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program compares short dna sequence with sub sequences of a long dna sequence,
    in order to find the sub sequences that best match the short dna sequence.
    """
    dna_search = input("please give me a DNA sequence to search: ")
    dna_search = dna_search.upper()
    dna_match = input("What DNA sequence would you like to match? ")
    dna_match = dna_match.upper()
    ans = best_matching_sequence(dna_search, dna_match)
    ans = ans.upper()
    print('The best match is ' + ans)


def best_matching_sequence(search, match):
    search_len = len(search)
    match_len = len(match)
    extra = search_len - match_len   # 多出來的DNA片段有幾個含氮鹼基
    max_percent = 0
    ans = ''
    for i in range(extra + 1):
        curr_percent = 0
        for j in range(match_len):
            if search[i+j] == match[j]:
                curr_percent += 100/match_len
        # print(search[i: i+match_len])  檢查用
        if curr_percent > max_percent:
            max_percent = curr_percent
            ans = search[i: i+match_len]
    return ans



# 另一種解法
# search = 'AaBBCDE'
# match = 'bbde'
# bestMatch = BCDE
#
#
# def best_match_substring(search, match):
#     search = search.upper()
#     match = match.upper()
#     max_percent = 0
#     best_match = ''
#     for i in range(len(match)):
#         curr_percent = match_percent(search[i: i+len(match)], match)
#         if curr_percent > max_percent:
#             max_percent = curr_percent
#             best_match = search[i: i + len(match)]
#     return best_match
#
#
# def match_percent(search, match):
#     matched = ''
#     for i in range(len(search)):
#         if search[i] == match[i]:
#             matched += search[i]
#     return len(matched)/len(search)  # percentage match
#
#
# best_match = best_match_substring(search, match)
# print('The best match is: ' + best_match)


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
