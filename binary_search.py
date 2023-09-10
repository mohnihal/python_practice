'''Binary Search'''

def BinarySearch(arr,low,high,x):
    if low<=high:
        mid = (high+low)//2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return BinarySearch(arr,mid+1,high,x)
        else:
            return BinarySearch(arr,low,mid-1,x)
    else:
        return -1

_array = [12,34,43,55,56,77,78,98]
print (BinarySearch(_array,0,len(_array)-1,43))