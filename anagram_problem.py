'''anagram problem'''
from collections import Counter

def anagram(string1,string2):
    if not string1 and string2:
        return

    count1 = Counter(string1)
    count2 = Counter(string2)
    count1.pop(' ', '')
    count2.pop(' ', '')
    print (count1==count2)

if __name__=="__main__":
    anagram("abcdef gh ij5 lm1 nokp","jklcabhg15imdefpn o")