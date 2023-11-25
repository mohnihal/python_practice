'''coin change algorithm'''
recursion_count = 0
def count(s,m,n):
    global recursion_count
    recursion_count+=1
    if n==0:
        print(s)
        return 1
    
    if n<0:
        return 0
    
    if m<=0 and n>=1:
        return 0
    
    return count(s, m-1, n) + count(s, m, n-s[m-1])


# print (count([1, 3, 5, 2, 6], 5, 9))
# print(recursion_count)
print (count([2, 5, 3, 6],4,10))

