'''coin change algorithm'''

def count(s,m,n):
    if n==0:
        return 1
    
    if n<0:
        return 0
    
    if m<=0 and n>=1:
        return 0
    
    return count(s,m-1,n) + count(s,m,n-s[m-1])


print (count([1, 3, 5, 2,6],5,9))
# print (count([1, 2, 3],2,3))

