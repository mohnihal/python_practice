def targetComputed(arr,target,combination):
    print (arr)
    print ("="*10)
    if not arr:
        return False
    arr_temp=arr[:]
    for item in arr:
        if target>item:
            combination.append(item)
            print ("item=",item,"  target=",target)
            print ("*"*10)
            diff= target-item
            print ("diff=",diff)
            arr_temp.remove(item)
            if diff in arr_temp:
                combination.append(diff)
                return True
            if targetComputed(arr_temp,diff,combination):
                return True
            combination.remove(item)
        else:
            pass
            # print ("item largeer than target:::")
    return False

combination=[]
print(targetComputed([12,4,9,3,5,7,11],18,combination))
print (combination)