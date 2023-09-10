class Solution:
    def __init__(self):
        self.closum=None
        self.clodif=None

    def computeTarget(self,arr,remaining,cursum,target):
        print (arr,remaining,cursum,self.closum,self.clodif)
        for each in range(0,len(arr)):
            if remaining==1:
                if abs(target-cursum-arr[each]) < self.clodif:
                    self.closum=cursum+arr[each]
                    self.clodif=abs(target-self.closum)
                    print ("closum changed")
                    print ("closum",self.closum)
                    print ("clodif",self.clodif)
            else:
                new_arr=arr[:]
                new_arr.pop(each)
                print (cursum+arr[each],new_arr,remaining-1)
                self.computeTarget(new_arr,remaining-1,cursum+arr[each],target)



    def threeSumClosest(self, nums,target):
        
        nums=sorted(nums)
        # print (nums)
        # print (nums[0],nums[1])
        self.closum=sum([nums[0],nums[1],nums[2]])
        self.clodif=abs(target-self.closum)
        self.computeTarget(nums,3,0,target)
        return self.closum,self.clodif



sol=Solution()
print (sol.threeSumClosest([1,1,1,0],100))



