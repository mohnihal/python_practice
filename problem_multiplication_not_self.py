from functools import reduce
class Solution:
    def productExceptSelf(self, nums):
        start_product=prev_product=1
        product_list = [start_product]*len(nums)
        product_list_reverse = [1]
        product_list_reverse.extend(nums)
        print (product_list_reverse)
        res=[]
        for i in range(len(nums)-1,-1,-1): 
            # print (i,product_list[i])
            if i!=len(nums)-1:
                product_list[i]=nums[i]*product_list[i+1]
            else:
                product_list[i]=nums[i]
        
        product_list.append(0)
        for each_index in range(0,len(nums)):
            # print (each_index)
            if not res:
                res.append(product_list[each_index+1])
            elif each_index==len(nums)-1:
                print ("g",each_index)
                print (product_list_reverse)
                product_list_reverse[each_index]=product_list_reverse[each_index]*product_list_reverse[each_index-1]
                res.append(product_list_reverse[each_index])
            else:
                if each_index>=1:
                    product_list_reverse[each_index]=product_list_reverse[each_index-1]*product_list_reverse[each_index]

                    res.append(product_list_reverse[each_index]*product_list[each_index+1])
                else:
                    res.append(product_list_reverse[each_index]*product_list[each_index+1])
            print (product_list_reverse)
            


        return res

sol=Solution()
print (sol.productExceptSelf([5,5]))



