'''Merge Sort'''

def Merge(ls,rs):
    # print(ls,rs)
    left_sorted_index = right_sorted_index = 0
    left_sorted_len, right_sorted_len = len(ls), len(rs)
    new_sorted_list = []
    for i in range(left_sorted_len + right_sorted_len):
        if left_sorted_index < left_sorted_len and right_sorted_index< right_sorted_len:
            if ls[left_sorted_index] <= rs[right_sorted_index]:
                new_sorted_list.append(ls[left_sorted_index])
                left_sorted_index+=1
            else:
                new_sorted_list.append(rs[right_sorted_index])
                right_sorted_index+=1
            
        elif left_sorted_index==left_sorted_len:
            new_sorted_list.append(rs[right_sorted_index])
            right_sorted_index+=1
        elif right_sorted_index==right_sorted_len:
            new_sorted_list.append(ls[left_sorted_index])
            left_sorted_index+=1

    return new_sorted_list


def MergeSort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums)//2

    left_sorted_list = MergeSort(nums[:mid])
    right_sorted_list = MergeSort(nums[mid:])

    return Merge(left_sorted_list,right_sorted_list)


random_list_of_nums = [120, 45, 68, 250, 176,33,100,550,222]
random_list_of_nums = MergeSort(random_list_of_nums)
print(random_list_of_nums)