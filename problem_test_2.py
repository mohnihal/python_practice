full_total=0
def targetComputed(arr,target,combination,total):
    global full_total
    print (arr)
    print ("="*10)

    # arr_temp=arr[:]
    if target==0:
        full_total+=1
        print ("returning 1")
        return 1
    
    if target <0:
        return 0
    for item in arr:
        if target>=item:
            print ("item=",item,"  target=",target)
            print ("*"*10)
            diff= target-item
            print ("diff=",diff)
            targetComputed(arr,diff,combination,total)

        else:
            pass

    return 0

combination=[]
# print(targetComputed([12,4,9,3,5,7,11],18,combination,0))
tot=0
print(targetComputed([1,2],4,combination,tot))
print ("full_total",full_total)