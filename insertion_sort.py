'''Insertion Sort'''


def InsertionSort(nums):
    for i in range(0,len(nums)-1):
        value_to_insert  = nums[i]
        j = i-1

        while j>=0 and nums[j]>value_to_insert:
            nums[j+1] = nums[j]
            j-=1
        
        nums[j+1] = value_to_insert