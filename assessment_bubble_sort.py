#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY plates as parameter.
#
def mergeSort(_arr,_stack,_left,_mid,_right):
    print (_arr,_stack,_left,_mid,_right)
    _num_inversions=0
    
    l = _left
    r = _right
    m = _mid
    
    while((l<=_mid-1) and (m<=_right)):
        if _arr[l] <= _arr[m]:
            _stack[r] = _arr[l]
            l+=1
            r+=1
        else:
            _stack[r] = _arr[m]
            r+=1
            m+=1
            
            _num_inversions = _num_inversions +(_mid-1)
            
    while l <= _mid-1:
        _stack[r] = _arr[l]
        r+=1
        l+=1
        
    while r <= _right:
        _stack[r] = _arr[m]
        r+=1
        m+=1
    
    for i in range(_left,_right+1,1):
        _arr[i] = _stack[i]
    
    # print (_num_inversions)
    return _num_inversions

def applyMergeSort(arr,st,left,right):
    num_inversions=0
    if right > left:
        mid = int((right+left)/2)
        
        num_inversions = applyMergeSort(arr,st,left,mid)
        num_inversions += applyMergeSort(arr,st,mid+1,right)
        
        num_inversions+=mergeSort(arr,st,left,mid+1,right)
    
    # print ("num_inversions",num_inversions) 
    return num_inversions
        
def getNumOfSwaps(nums,n):
    stack = [0 for i in range(n)]
    sortList = applyMergeSort(nums,stack,0,n-1) 
    # print ("sortList",sortList)
    return sortList
    
def getMinMoves(plates):
    # Write your code here
    swap_count = getNumOfSwaps(plates,len(plates))
    return swap_count



if __name__ == '__main__':
    getMinMoves([2,4,1,3,6])