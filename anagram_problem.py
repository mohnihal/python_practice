'''anagram problem'''
from collections import Counter

def anagram(string1,string2):
    if not string1 and string2:
        return

    count1 = Counter
    count2 = Counter
    count1 = count1(string1.replace(" ",""))
    count2 = count2(string2.replace(" ",""))
    print (count1==count2)
    print (count1)
    print (count2)

if __name__=="__main__":
    anagram("abcdef gh ij5 lm1 nokp","jklcabhg15imdefpn o")