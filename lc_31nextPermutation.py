
class Solution(object):
    def nextPermutation(self, nums):
        """
        step1: find the first decreaing ele (from end to begin), say i 
        step2: find increasing ele after i,but is the min say j 
        swap(i,j)

        eg. 
        [6,2,1,5,4,3,0]
             v
             here, we have choice set{0,1,3,4,5}, the next possible is 3, which is greater but the min possible one.
        
        """
        def f(i):

            a = sorted(nums[i+1:])
            for dx,v in enumerate(a):
                nums[i+1+dx] = v
            return nums

        i,j = -1,-1
        pre = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            cur = nums[i]
            if cur < pre:
              
                target = [float('inf'),i]
                for j in range(i+1, len(nums)):
                    if nums[j] > cur:
                        if target[0] > nums[j]:
                            target = [nums[j], j]
                
                nums[i], nums[target[1]] =  nums[target[1]],nums[i]
               
                return f(i)
            pre = cur
 
        nums.sort()
        return nums
