"""Program to find all combinations of number that would return a sum x"""

list_of_combs = []
combs_count = 0
main_array = [2, 5, 3, 1, 4, 6, 8]
def find_all_possibilities(array, summated_array, target):
    global combs_count
    global main_array
 
    if target == 0:
        # success_list = [i for i in main_array if i not in array]
        if set(summated_array) not in list_of_combs:
            list_of_combs.append(set(summated_array))
            combs_count+=1
        else:
            print(f"repetition:{summated_array}")
        return
    for i in array:
        if i<=target and set(summated_array+[i]) not in list_of_combs:
            find_all_possibilities([j for j in array if j !=i], summated_array+[i], target-i)

find_all_possibilities(main_array, [], 12)
print(list_of_combs)
print(combs_count)