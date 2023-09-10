'''Selection Sort'''

def SelectionSort(nums):
    for i in range(len(nums)):
        lowest_value_index=i

        for j in range(i+1,len(nums)):
            if nums[lowest_value_index] > nums[j]:
                lowest_value_index=j

        
        nums[i],nums[lowest_value_index]=nums[lowest_value_index],nums[i]
    
    return (nums)


random_list_of_nums = [12, 8, 3, 20, 11]
SelectionSort(random_list_of_nums)
print(random_list_of_nums)
