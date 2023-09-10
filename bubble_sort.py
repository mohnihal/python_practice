'''Bubble Sort'''

def BubbleSort(nums):
    swapped=True
    while swapped:
        swapped=False
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                swapped=True

    return nums


random_list_of_nums = [2,4,3,1,6]
print(BubbleSort(random_list_of_nums))