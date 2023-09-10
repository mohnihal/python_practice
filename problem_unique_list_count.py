from email.quoprimime import unquote


def Solution(nums,k):
    unique_set=set()
    for n in nums:
        diff=n-k
        tup=(n,diff)
        # print (tup)
        if diff in nums and diff>0 and tup not in unique_set:
            unique_set.add((n,diff))
            # print (unique_set)
    return len(unique_set)


print (Solution([1,2,5,6,9,10],2))