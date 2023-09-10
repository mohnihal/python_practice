# from lib2to3.pgen2.token import EQUAL


# def solution(after):
#     print (after)
#     cur_sum=0
#     before=after[:]
#     for i in range(len(after)):
#         # print (i)
#         for j in range(len(after[i])):
#             print (j)
#             if i==0 and j==0:
#                 before[i][j]=after[i][j]
#                 print ("both zero")
#                 print (before[i][j])
#             elif j==len(after[i])-1 or i==0:
#                 before[i][j]=after[i][j]-cur_sum
#                 print ("both EQUAL")
#                 print (before[i][j])
#             else:
#                 before[i][j]=after[i][j]-sum(after[x][j] for x in range(0,i))
#                 print ("else")
#                 print (before[i][j])

#             # print (before[i][j])
#             cur_sum+=before[i][j]

#     return before


# print (solution([[14,9,9,16,16], 
#  [2,12,0,5,20], 
#  [1,2,13,12,0], 
#  [20,5,0,15,10], 
#  [16,5,4,4,0], 
#  [1,16,19,2,18]]))


# def solution(a,m):
#     max_val=min(a)
#     # print (max_val)
#     for i in range(0,len(a)-m+1):
#         # print (min(a[i:i+m])
#         max_val=max(max_val,min(a[i:i+m]))
#     return max_val

# print (solution([2, 5, 4, 6, 8],1))

# def solution(arr, n):
#     while arr:
#         if n in arr:
#             arr.remove(n)
#             n=n*2
#         else:
#             return n
#     return n

# print (solution([39],39))


# def maxProfit(prices,numT):
#     """
#     :type prices: List[int]
#     :rtype: int
#     """
#     l,r=0,1
#     maxP=[0]
#     # numT = 5
#     while r<len(prices):
#         print (prices[l],prices[r])
#         if prices[l] < prices[r]:
#             profit=prices[r]-prices[l]
#             if profit>maxP[-1]:
#                 if profit>maxP[0]:
#                     maxP.insert(0,profit)
#                     if len(maxP)>numT:
#                         maxP.pop()
#                 elif len(maxP)>numT:
#                     maxP.pop()
#                     maxP.append(profit)
#                     maxP.sort(reverse=True)
#                 else:
#                     maxP.append(profit)
#                     maxP.sort(reverse=True)
#             elif len(maxP)<numT:
#                 maxP.append(profit)
#                 maxP.sort(reverse=True)

#             # maxP=max(profit,maxP)
#         else:
#             l=r
#         r+=1
#         print (profit)
#         print (maxP,"maxP")
#     return maxP

# print (maxProfit([100, 200, 1300, 400, 500, 600, 1000],2))


def findMaxProfit(prices,k):

    if not len(prices):
        return 0


    profits = [[0 for d in prices] for t in range(k+1)]
    # profits = [[0]*len(prices)]*(k+1)
    print (profits)
    for t in range(1,k+1):
        maxP = float("-inf")
        print (maxP)

        for d in range(1,len(prices)):
            print (profits[t-1][d-1]-prices[d-1],"diff")
            maxP = max(maxP,profits[t-1][d-1]-prices[d-1])
            profits[t][d] = max(profits[t][d-1],maxP+prices[d])
            print ("profits",profits)

    return profits[-1][-1]


print (findMaxProfit([100, 200, 1300, 400, 500, 600, 1000],2))